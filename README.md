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
```

### 2. Install Required Dependencies

Run the following command to install all required Python packages:

```bash
python3 -m pip install SpeechRecognition librosa scipy scikit-learn soundfile
```

Breaking down the packages:
- **SpeechRecognition** - For audio recording from microphone
- **librosa** - For audio feature extraction and analysis
- **scipy** - For scientific computing and distance calculations
- **scikit-learn** - For machine learning utilities
- **soundfile** - For proper audio file handling (suppresses warnings)

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/tanyaeveritt/what_counter.git
cd what_counter
```

### 2. Install Dependencies

```bash
python3 -m pip install SpeechRecognition librosa scipy scikit-learn soundfile
```

### 3. Prepare Your Reference Audio

Place your reference audio file in the project directory and name it `what.m4a`. This can be:
- A recording of yourself saying "what"
- An audio file with the pronunciation you want to match
- Any `.m4a`, `.wav`, `.mp3`, or other common audio format

### 4. Run the Program

```bash
python3 audio_what_counter.py
```

## Usage

### Running the Program

Once you have the dependencies installed and `what.m4a` in the correct location:

```bash
python3 audio_what_counter.py
```

### Interactive Commands

Once the program is running, use these commands at the prompt:

- **`status`** - Display current match count and session duration
- **`reset`** - Clear the counter and start fresh
- **`quit`** - Stop listening and exit the program

### Example Session

```
🎙️  What Counter - Audio Listener
========================================
✅ Reference audio loaded from: what.m4a

⏳ Listening... ✓ Got audio!
✅ MATCH! | Total: 1

⏳ Listening... ✓ Got audio!
⚠️  No match

(Commands: 'status', 'reset', 'quit'): status

📊 Status:
   Total matches: 1
   Session time: 0:00:15.234567

(Commands: 'status', 'reset', 'quit'): quit

👋 Stopping listener...
========================================
📈 Final Count: 1
   Session duration: 0:00:20.456789
========================================
```

## How It Works

1. **Initialization**: The program loads your reference audio file (`what.m4a`) and extracts its acoustic features using MFCC (Mel-frequency cepstral coefficients) analysis
2. **Calibration**: Microphone noise levels are automatically calibrated for 2 seconds at startup
3. **Listening**: Continuously listens for audio input from your microphone in real-time
4. **Analysis**: Compares incoming audio against the reference using cosine similarity
5. **Counting**: If similarity is ≥90%, increments the counter and logs the match
6. **Feedback**: Displays real-time feedback about matches and no-matches

### Audio Similarity Algorithm

- Uses MFCC (Mel-Frequency Cepstral Coefficients) to extract acoustic features
- Compares features using cosine distance metric
- Similarity score ranges from 0 (completely different) to 1 (identical)
- Matches are counted when similarity ≥ 0.90 (90%)

## Troubleshooting

### "ModuleNotFoundError" when running the script

Make sure all dependencies are installed:
```bash
python3 -m pip install SpeechRecognition librosa scipy scikit-learn soundfile
```

Verify installation:
```bash
python3 -m pip list
```

### "Could not load reference audio" error

- Ensure `what.m4a` exists in the same directory as `audio_what_counter.py`
- Check that the file is a valid audio format
- If using an unsupported format, convert to `.wav` or `.mp3`:
  ```bash
  ffmpeg -i your_file.m4a what.m4a
  ```

### Microphone not detected

- Check that your microphone is connected and working
- Verify microphone permissions:
  - **macOS**: System Preferences → Security & Privacy → Microphone
  - **Windows**: Settings → Privacy & security → Microphone
  - **Linux**: Check ALSA or PulseAudio settings
- Try using a different microphone or USB audio device

### WaitTimeoutError or listening issues

- Move closer to your microphone
- Reduce background noise in your environment
- The app will automatically retry on timeout
- Adjust microphone sensitivity in your OS settings

### "PySoundFile failed" warnings

Install the soundfile package to suppress these warnings:
```bash
python3 -m pip install soundfile
```

### Program crashes or hangs

- Make sure you have enough free RAM
- Close other applications using the microphone
- Try restarting the program
- Check for updates to Python and dependencies

## File Structure

```
what_counter/
├── audio_what_counter.py    # Main program
├── what.m4a                 # Reference audio file (you provide this)
├── README.md                # This file
└── .gitignore               # (optional) Git ignore file
```

## System Requirements

| Requirement | Specification |
|-----------|---------------|
| **OS** | macOS, Windows, or Linux |
| **Python** | 3.7 or higher |
| **RAM** | 512 MB minimum |
| **Storage** | 100 MB for dependencies |
| **Microphone** | Any standard audio input device |

## Performance Notes

- The first run may take a few seconds to load and calibrate the microphone
- Accuracy depends on microphone quality and environment noise levels
- MFCC analysis works best with speech-like audio
- The >90% similarity threshold can be adjusted in the code if needed
- Processing happens in real-time with minimal latency

## Customization

### Adjusting Similarity Threshold

To change the matching threshold from 90%, edit line 77 in `audio_what_counter.py`:

```python
if similarity_score is not None and similarity_score >= 0.90:  # Change 0.90 to your desired threshold
```

### Changing Reference Audio File Name

Edit line 21 in `audio_what_counter.py`:

```python
self.load_reference_audio("what.m4a")  # Change to your filename
```

## Supported Audio Formats

The program supports any audio format that librosa can read:
- `.wav` - WAV format (recommended)
- `.mp3` - MPEG-3
- `.m4a` - MPEG-4 Audio
- `.flac` - Free Lossless Audio Codec
- `.ogg` - Ogg Vorbis
- And many others

## License

This project is open source and available for personal use.

## Author

Created by Tanya Everitt

## Support

If you encounter issues:

1. Verify all dependencies are installed:
   ```bash
   python3 -m pip list
   ```

2. Ensure `what.m4a` is in the correct location (same directory as the script)

3. Check microphone permissions and connectivity

4. Try running with a quieter environment

5. Check the [Troubleshooting](#troubleshooting) section above

6. Open an issue on GitHub if the problem persists

## Contributing

Feel free to fork this repository and submit pull requests with improvements!

## Changelog

### Version 1.0
- Initial release
- Audio similarity matching using MFCC
- Real-time listening and counting
- Interactive command interface
- Session statistics