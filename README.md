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

### Quick Start (Simple Function)

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

### Command Line Usage

```bash
# Run with default settings
python whitenoise.py

# Stop with Ctrl+C (Cmd+C on Mac)
```

## ⚙️ Configuration Options

### Sample Rate
- **44100 Hz** (default): CD quality, recommended for most uses
- **48000 Hz**: Professional audio standard
- **22050 Hz**: Lower quality, reduced CPU usage

### Block Size
- **1024** (default): Good balance of latency and performance
- **512**: Lower latency, higher CPU usage
- **2048**: Higher latency, lower CPU usage

### Amplitude
- **0.1** (default): Safe starting volume
- **Range**: 0.0 (silent) to 1.0 (maximum)
- **Recommendation**: Start low and gradually increase

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

## 📚 Recommended Usage Patterns

### For Sleep
```python
# Gentle settings for nighttime use
generator = StereoWhiteNoiseGenerator(amplitude=0.05)
generator.start()
# Let it run all night, stop in the morning
```

### For Concentration
```python
# Moderate settings for work/study
generator = StereoWhiteNoiseGenerator(amplitude=0.08)
generator.start()
# Use during work sessions, take breaks every hour
```

### For Tinnitus Relief
```python
# Customizable settings - adjust to mask tinnitus frequency
generator = StereoWhiteNoiseGenerator(amplitude=0.12)
generator.start()
# Consult with audiologist for optimal settings
```

## ⚕️ Disclaimer

This software is not a medical device and is not intended to diagnose, treat, cure, or prevent any medical condition. For serious sleep disorders, tinnitus, or other health concerns, please consult qualified healthcare professionals.
