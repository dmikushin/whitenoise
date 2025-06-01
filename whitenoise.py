import sounddevice as sd
import numpy as np
import time
import argparse
import sys

# Preset configurations for common use cases
PRESETS = {
    'sleep': {
        'description': 'Gentle settings optimized for sleep and relaxation',
        'sample_rate': 44100,
        'block_size': 1024,
        'amplitude': 0.05
    },
    'concentration': {
        'description': 'Moderate settings ideal for work and study',
        'sample_rate': 44100,
        'block_size': 1024,
        'amplitude': 0.08
    },
    'tinnitus': {
        'description': 'Higher amplitude settings for tinnitus masking',
        'sample_rate': 44100,
        'block_size': 1024,
        'amplitude': 0.12
    },
    'default': {
        'description': 'Balanced settings suitable for general use',
        'sample_rate': 44100,
        'block_size': 1024,
        'amplitude': 0.1
    }
}

def parse_arguments():
    """Parse command line arguments for the white noise generator."""
    parser = argparse.ArgumentParser(
        description='Stereo White Noise Generator - Therapeutic audio for sleep, concentration, and tinnitus relief',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Preset Modes:
  sleep         Gentle settings for sleep and relaxation (amplitude: 0.05)
  concentration Moderate settings for work and study (amplitude: 0.08)
  tinnitus      Higher amplitude for tinnitus masking (amplitude: 0.12)
  default       Balanced settings for general use (amplitude: 0.1)

Examples:
  %(prog)s                          # Use default preset
  %(prog)s --preset sleep           # Use sleep preset
  %(prog)s --amplitude 0.15         # Custom amplitude with default preset
  %(prog)s --preset tinnitus -a 0.2 # Tinnitus preset with custom amplitude
  %(prog)s -s 48000 -b 2048 -a 0.06 # Fully custom settings

Safety Note:
  Always start with low amplitudes and protect your hearing.
  Recommended maximum amplitude is 0.2 for extended use.
        '''
    )
    
    # Preset selection
    parser.add_argument(
        '--preset', '-p',
        choices=list(PRESETS.keys()),
        default='default',
        help='Select a preset mode (default: %(default)s)'
    )
    
    # Audio configuration options
    parser.add_argument(
        '--sample-rate', '-s',
        type=int,
        choices=[22050, 44100, 48000],
        help='Audio sample rate in Hz (default: preset dependent)'
    )
    
    parser.add_argument(
        '--block-size', '-b',
        type=int,
        choices=[256, 512, 1024, 2048, 4096],
        help='Audio block size in frames (default: preset dependent). '
             'Lower values = lower latency, higher CPU usage'
    )
    
    parser.add_argument(
        '--amplitude', '-a',
        type=float,
        metavar='0.0-1.0',
        help='Noise amplitude (0.0 = silent, 1.0 = maximum). '
             'Default: preset dependent. Start low for safety!'
    )
    
    # Information options
    parser.add_argument(
        '--list-presets',
        action='store_true',
        help='List all available presets and their settings'
    )
    
    parser.add_argument(
        '--list-devices',
        action='store_true',
        help='List available audio devices'
    )
    
    parser.add_argument(
        '--quiet', '-q',
        action='store_true',
        help='Minimize output messages'
    )
    
    return parser.parse_args()

def validate_amplitude(amplitude):
    """Validate and clamp amplitude to safe range."""
    if amplitude < 0.0:
        print("Warning: Amplitude cannot be negative. Setting to 0.0")
        return 0.0
    elif amplitude > 1.0:
        print("Warning: Amplitude cannot exceed 1.0. Setting to 1.0")
        return 1.0
    elif amplitude > 0.5:
        print(f"Warning: High amplitude ({amplitude}) detected. Please protect your hearing!")
    return amplitude

def list_presets():
    """Display all available presets and their configurations."""
    print("Available Presets:")
    print("=" * 60)
    for name, config in PRESETS.items():
        print(f"\n{name.upper()}:")
        print(f"  Description: {config['description']}")
        print(f"  Sample Rate: {config['sample_rate']} Hz")
        print(f"  Block Size:  {config['block_size']} frames")
        print(f"  Amplitude:   {config['amplitude']}")

def list_audio_devices():
    """Display available audio devices."""
    try:
        print("Available Audio Devices:")
        print("=" * 40)
        devices = sd.query_devices()
        for i, device in enumerate(devices):
            device_type = []
            if device['max_inputs'] > 0:
                device_type.append('input')
            if device['max_outputs'] > 0:
                device_type.append('output')
            
            print(f"{i:2d}: {device['name']}")
            print(f"     Type: {', '.join(device_type)}")
            print(f"     Channels: {device['max_outputs']} out, {device['max_inputs']} in")
            print(f"     Sample Rate: {device['default_samplerate']} Hz")
            print()
    except Exception as e:
        print(f"Error listing audio devices: {e}")

class StereoWhiteNoiseGenerator:
    def __init__(self, sample_rate=44100, block_size=1024, amplitude=0.1):
        """
        Initialize the white noise generator.
        
        Args:
            sample_rate (int): Sample rate in Hz (default: 44100)
            block_size (int): Number of frames per block (default: 1024)
            amplitude (float): Amplitude of the noise (0.0 to 1.0, default: 0.1)
        """
        self.sample_rate = sample_rate
        self.block_size = block_size
        self.amplitude = amplitude
        self.stream = None
        self.running = False
    
    def audio_callback(self, outdata, frames, time, status):
        """
        Callback function that generates white noise for each audio block.
        """
        if status:
            print(f"Audio status: {status}")
        
        # Generate random white noise for stereo (2 channels)
        # Shape: (frames, 2) for stereo output
        noise = np.random.uniform(-1, 1, (frames, 2)) * self.amplitude
        
        # Copy noise to output buffer
        outdata[:] = noise
    
    def start(self):
        """Start the white noise generator."""
        if self.running:
            print("Generator is already running!")
            return
        
        try:
            # Create and start the audio stream
            self.stream = sd.OutputStream(
                samplerate=self.sample_rate,
                blocksize=self.block_size,
                channels=2,  # Stereo output
                callback=self.audio_callback,
                dtype=np.float32
            )
            
            self.stream.start()
            self.running = True
            print(f"Stereo white noise generator started!")
            print(f"Sample rate: {self.sample_rate} Hz")
            print(f"Block size: {self.block_size} frames")
            print(f"Amplitude: {self.amplitude}")
            print("Playing infinitely until interrupted...")
            
        except Exception as e:
            print(f"Error starting audio stream: {e}")
            self.running = False
    
    def stop(self):
        """Stop the white noise generator."""
        if self.stream and self.running:
            self.stream.stop()
            self.stream.close()
            self.running = False
            print("White noise generator stopped.")
    
    def set_amplitude(self, amplitude):
        """
        Change the amplitude of the white noise.
        
        Args:
            amplitude (float): New amplitude (0.0 to 1.0)
        """
        self.amplitude = max(0.0, min(1.0, amplitude))
        print(f"Amplitude set to: {self.amplitude}")

def main():
    """Main function to run the white noise generator with CLI support."""
    args = parse_arguments()
    
    # Handle information requests
    if args.list_presets:
        list_presets()
        return
    
    if args.list_devices:
        list_audio_devices()
        return
    
    # Get base configuration from selected preset
    config = PRESETS[args.preset].copy()
    
    # Override with any custom arguments provided
    if args.sample_rate is not None:
        config['sample_rate'] = args.sample_rate
    
    if args.block_size is not None:
        config['block_size'] = args.block_size
    
    if args.amplitude is not None:
        config['amplitude'] = validate_amplitude(args.amplitude)
    else:
        config['amplitude'] = validate_amplitude(config['amplitude'])
    
    # Display configuration if not in quiet mode
    if not args.quiet:
        print(f"White Noise Generator - {args.preset.upper()} mode")
        print("=" * 50)
        print(f"Preset: {args.preset} - {PRESETS[args.preset]['description']}")
        print(f"Sample Rate: {config['sample_rate']} Hz")
        print(f"Block Size: {config['block_size']} frames")
        print(f"Amplitude: {config['amplitude']}")
        print("=" * 50)
    
    # Create generator with configured settings
    generator = StereoWhiteNoiseGenerator(
        sample_rate=config['sample_rate'],
        block_size=config['block_size'],
        amplitude=config['amplitude']
    )
    
    try:
        generator.start()
        
        if not args.quiet:
            print("White noise is playing infinitely. Press Ctrl+C to stop.")
            print("Safety reminder: Take breaks and protect your hearing!")
        
        # Keep the program running infinitely until user interruption
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        if not args.quiet:
            print("\nUser interrupted. Stopping white noise...")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
    finally:
        generator.stop()

# Alternative: Create a simple infinite white noise function
def infinite_white_noise(amplitude=0.1, sample_rate=44100):
    """
    Simple function to play white noise infinitely until interrupted.
    
    Args:
        amplitude (float): Amplitude (0.0 to 1.0)
        sample_rate (int): Sample rate in Hz
    """
    def callback(outdata, frames, time, status):
        outdata[:] = np.random.uniform(-1, 1, (frames, 2)) * amplitude
    
    print(f"Playing stereo white noise infinitely at amplitude {amplitude}...")
    print("Press Ctrl+C to stop.")
    
    try:
        with sd.OutputStream(channels=2, callback=callback, samplerate=sample_rate):
            while True:
                time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopped by user.")

if __name__ == "__main__":
    # Run the main infinite generator
    main()
