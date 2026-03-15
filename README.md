# audio_what_counter.py Documentation

## Overview
The `audio_what_counter.py` file is designed to analyze audio input and provide insights on various metrics related to audio processing. It has applications in fields such as sound analysis, music information retrieval, and audio-based data analytics.

## Prerequisites
Before running the script, ensure you have the following prerequisites installed:
- Python 3.6 or higher
- Necessary libraries:
  - numpy
  - scipy
  - librosa
  - matplotlib

You can install these libraries using pip:
```bash
pip install numpy scipy librosa matplotlib
```

## Installation
To use the `audio_what_counter.py`, first clone the repository:
```bash
git clone https://github.com/tanyaeveritt/what_counter.git
cd what_counter
```

## How to Run
To execute the script, use the following command in your terminal:
```bash
python audio_what_counter.py <path_to_audio_file>
```
Replace `<path_to_audio_file>` with the actual path to the audio file you want to analyze.

## Example
For example, if you have an audio file `example.wav`, you would run:
```bash
python audio_what_counter.py example.wav
```

## Output
The script will output metrics such as:
- Duration of the audio
- Sample rate
- Number of channels
- Spectral features
- Any other metrics defined in the script.

## Contribution
Please feel free to submit a pull request if you would like to contribute to the project.

## License
This project is licensed under the MIT License.