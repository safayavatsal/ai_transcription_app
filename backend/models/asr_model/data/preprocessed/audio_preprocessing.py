import librosa
import numpy as np

def preprocess_audio(file_path):
    y, sr = librosa.load(file_path, sr=16000)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    return mfcc

# Example usage:
# mfcc_features = preprocess_audio('/path/to/audio/file.wav')
