# Stereo White Noise Generator

A Python-based therapeutic white noise generator designed to provide continuous, high-quality stereo white noise for various therapeutic and wellness applications.

## 🎯 Purpose & Therapeutic Benefits

White noise has been scientifically proven to offer numerous therapeutic benefits:

- **Sleep Enhancement**: Masks disruptive environmental sounds, promoting deeper and more restful sleep
- **Concentration & Focus**: Creates a consistent auditory backdrop that helps reduce distractions
- **Tinnitus Relief**: Provides masking sounds that can help alleviate ringing in the ears
- **Stress Reduction**: Creates a calming environment that can help reduce anxiety and stress
- **Baby Sleep Aid**: Mimics womb sounds, helping infants fall asleep and stay asleep longer
- **Study & Work**: Improves cognitive performance by blocking intermittent noise distractions

## ✨ Features

- **High-Quality Stereo Output**: Generates true stereo white noise for immersive audio experience
- **Infinite Playback**: Runs continuously until manually stopped
- **Configurable Parameters**: Adjustable sample rate, block size, and amplitude
- **Real-Time Generation**: Low-latency audio processing for immediate response
- **Safety Controls**: Built-in amplitude limiting to protect hearing
- **Multiple Interface Options**: Both class-based and function-based implementations
- **Cross-Platform**: Works on Windows, macOS, and Linux

## 📋 Requirements

- Python 3.6 or higher
- NumPy
- sounddevice

## 🚀 Installation

1. **Clone or download the repository**
   ```bash
   git clone <repository-url>
   cd white-noise-generator
   ```

2. **Install required dependencies**
   ```bash
   pip install numpy sounddevice
   ```

3. **Verify audio system compatibility**
   ```bash
   python -c "import sounddevice as sd; print(sd.query_devices())"
   ```

## 🎵 Usage

### Command Line Interface

The white noise generator includes a comprehensive CLI with preset modes and full customization options.

#### Quick Start with Presets

```bash
# Use default settings
python whitenoise.py

# Sleep mode - gentle, low amplitude for nighttime use
whitenoise --preset sleep

# Concentration mode - moderate settings for work/study
whitenoise --preset concentration

# Tinnitus relief mode - higher amplitude for masking
whitenoise --preset tinnitus
```

Stop with Ctrl+C (Cmd+C on Mac).

#### Custom Settings

```bash
# Custom amplitude with a preset
whitenoise --preset sleep --amplitude 0.03

# Fully custom settings
whitenoise --sample-rate 48000 --block-size 2048 --amplitude 0.15

# High-performance settings (lower latency)
whitenoise -s 44100 -b 512 -a 0.08

# Quiet mode (minimal output)
whitenoise --preset concentration --quiet
```

#### ⚙️ Settings Guidelines

Sample Rate:
- **44100 Hz** (default): CD quality, recommended for most uses
- **48000 Hz**: Professional audio standard
- **22050 Hz**: Lower quality, reduced CPU usage

Block Size:
- **1024** (default): Good balance of latency and performance
- **512**: Lower latency, higher CPU usage
- **2048**: Higher latency, lower CPU usage

Amplitude:
- **0.1** (default): Safe starting volume
- **Range**: 0.0 (silent) to 1.0 (maximum)
- **Recommendation**: Start low and gradually increase


#### Information Commands

```bash
# List all available presets
whitenoise --list-presets

# List available audio devices
whitenoise --list-devices

# Show help and all options
whitenoise --help
```

#### CLI Options Reference

| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `--preset` | `-p` | Select preset mode (sleep, concentration, tinnitus, default) | default |
| `--sample-rate` | `-s` | Sample rate: 22050, 44100, or 48000 Hz | Preset dependent |
| `--block-size` | `-b` | Block size: 256, 512, 1024, 2048, or 4096 frames | Preset dependent |
| `--amplitude` | `-a` | Amplitude: 0.0 to 1.0 | Preset dependent |
| `--quiet` | `-q` | Minimize output messages | False |
| `--list-presets` | | Show all presets and exit | |
| `--list-devices` | | Show audio devices and exit | |

### Preset Modes

| Preset | Amplitude | Use Case | Description |
|--------|-----------|----------|-------------|
| **sleep** | 0.05 | Nighttime rest | Gentle, soothing white noise for sleep |
| **concentration** | 0.08 | Work/Study | Moderate masking for focus and productivity |
| **tinnitus** | 0.12 | Tinnitus relief | Higher amplitude for symptom masking |
| **default** | 0.10 | General use | Balanced settings for everyday use |

### Programmatic Usage (Advanced)

```python
from whitenoise import infinite_white_noise

# Start infinite white noise with default settings
infinite_white_noise()
```

### Advanced Usage (Class-Based)

```python
from whitenoise import StereoWhiteNoiseGenerator

# Create generator with custom settings
generator = StereoWhiteNoiseGenerator(
    sample_rate=44100,   # CD quality
    block_size=1024,     # Low latency
    amplitude=0.1        # Safe volume level
)

# Start the generator
generator.start()

# Adjust volume during playback
generator.set_amplitude(0.15)

# Stop when needed
generator.stop()
```

## 🛡️ Safety Guidelines

⚠️ **Important Safety Information**

- **Start with low volume**: Always begin with amplitude 0.1 or lower
- **Protect your hearing**: Prolonged exposure to loud white noise can damage hearing
- **Take breaks**: Use for reasonable durations with periodic breaks
- **Monitor volume levels**: Be aware of your audio system's output volume
- **Consult professionals**: For therapeutic use, consider consulting audiologists or sleep specialists

## 🔧 Troubleshooting

### Common Issues

**"No audio output"**
- Check if your audio device is properly connected
- Verify audio drivers are installed and up to date
- Run `python -c "import sounddevice as sd; print(sd.query_devices())"` to list available devices

**"Audio stuttering or crackling"**
- Increase block size (e.g., 2048 or 4096)
- Close other audio applications
- Check CPU usage and close unnecessary programs

**"PortAudio error"**
- Update sounddevice: `pip install --upgrade sounddevice`
- On Linux, install PortAudio: `sudo apt-get install portaudio19-dev`
- On macOS, install via Homebrew: `brew install portaudio`

**"Permission denied" errors**
- On macOS/Linux, ensure microphone/audio permissions are granted
- Run with appropriate permissions if needed

### Performance Optimization

- **Lower CPU usage**: Increase block size to 2048 or 4096
- **Lower latency**: Decrease block size to 512 (higher CPU usage)
- **Memory efficiency**: The generator uses minimal memory as it generates noise in real-time

## 🧬 Technical Details

### Audio Specifications
- **Channels**: 2 (stereo)
- **Bit Depth**: 32-bit floating point
- **Noise Type**: Uniform distribution white noise
- **Frequency Range**: Full spectrum (20 Hz - 22 kHz at 44.1 kHz sample rate)

### Algorithm
The generator uses NumPy's `random.uniform()` function to create noise with uniform distribution between -1 and 1, which is then scaled by the amplitude parameter and output to both stereo channels.

## ⚕️ Disclaimer

This software is not a medical device and is not intended to diagnose, treat, cure, or prevent any medical condition. For serious sleep disorders, tinnitus, or other health concerns, please consult qualified healthcare professionals.
