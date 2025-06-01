import sounddevice as sd
import numpy as np
import time

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
    """Main function to run the white noise generator infinitely."""
    # Create generator with default settings
    # You can adjust these parameters:
    generator = StereoWhiteNoiseGenerator(
        sample_rate=44100,   # Standard CD quality
        block_size=1024,     # Good balance of latency and performance
        amplitude=0.1        # Start with low volume for safety
    )
    
    try:
        generator.start()
        
        # Keep the program running infinitely until user interruption
        print("White noise is playing infinitely. Press Ctrl+C to stop.")
        while True:
            time.sleep(1)  # Sleep longer since we're running infinitely
            
    except KeyboardInterrupt:
        print("\nUser interrupted. Stopping white noise...")
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
