"""
Stereo White Noise Generator

A Python-based therapeutic white noise generator designed to provide continuous,
high-quality stereo white noise for various therapeutic and wellness applications.

Classes:
    StereoWhiteNoiseGenerator: Main class for generating white noise

Functions:
    infinite_white_noise: Simple function for infinite white noise playback
    main: CLI entry point with preset modes and custom settings
"""

__version__ = "1.0.0"
__author__ = "Dmitry Mikushin"
__email__ = "dmitry@kernelgen.org"

from .whitenoise import StereoWhiteNoiseGenerator, infinite_white_noise, main

__all__ = [
    "StereoWhiteNoiseGenerator",
    "infinite_white_noise", 
    "main",
    "__version__",
    "__author__",
    "__email__"
]
