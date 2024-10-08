import os

import librosa  # For audio processing
import numpy as np


def load_data(audio_dir, transcription_dir):
    audio_files = []
    transcriptions = []
    
    for filename in os.listdir(audio_dir):
        if filename.endswith('.wav'):
            audio_files.append(os.path.join(audio_dir, filename))
            with open(os.path.join(transcription_dir, filename.replace('.wav', '.txt')), 'r') as f:
                transcriptions.append(f.read().strip())
    
    return audio_files, transcriptions

def preprocess_data(audio_files, transcriptions):
    X = []
    y = []
    
    for audio_file, transcription in zip(audio_files, transcriptions):
        audio, sr = librosa.load(audio_file, sr=16000)
        audio = librosa.feature.mfcc(audio, sr=sr, n_mfcc=13)  # Example feature extraction
        X.append(audio)
        y.append(transcription)  # Encode transcription to integers if necessary

    return {'X': np.array(X), 'y': np.array(y)}

def save_model(model, model_path):
    model.save(model_path)

