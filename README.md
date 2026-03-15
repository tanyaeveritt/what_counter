# 🎙️ What Counter - Audio Listener

A Python application that listens to live audio and counts instances of spoken words that sound similar to a reference audio file (>90% acoustic similarity).

## Overview

This program continuously monitors your microphone and compares incoming audio against a reference audio file (`what.m4a`). When it detects audio that is more than 90% acoustically similar to the reference, it increments a counter and logs the match.

### Key Features

- 🎤 **Real-time audio listening** from your microphone
- 🎯 **Acoustic similarity matching** using MFCC (Mel-frequency cepstral coefficients)
- 📊 **Live counter** displaying matches as they occur
- 💾 **Session statistics** with total match count and duration
- 🔧 **Interactive commands** for status, reset, and quit

## Prerequisites

- Python 3.7 or higher
- A microphone connected to your computer
- A reference audio file named `what.m4a` in the same directory as the script

## Installation

### 1. Install Python 3

Make sure you have Python 3 installed. Check your version:

```bash
python3 --version
