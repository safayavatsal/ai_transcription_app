import os

import librosa  # For audio processing
import numpy as np


def load_data(text_dir, audio_dir):
    text_samples = []
    audio_clips = []
    
    for filename in os.listdir(text_dir):
        if filename.endswith('.txt'):
            with open(os.path.join(text_dir, filename), 'r') as f:
                text_samples.append(f.read().strip())
            audio_file = os.path.join(audio_dir, filename.replace('.txt', '.wav'))
            audio_clips.append(audio_file)
    
    return text_samples, audio_clips

def preprocess_data(text_samples, audio_clips):
    X = []
    y = []
    
    for text_sample, audio_clip in zip(text_samples, audio_clips):
        audio, sr = librosa.load(audio_clip, sr=22050)
        audio = librosa.feature.mfcc(audio, sr=sr, n_mfcc=13)  # Example feature extraction
        X.append(text_sample)  # Convert text to features (e.g., tokenization)
        y.append(audio)  # This would be your target audio features

    return {'X': np.array(X), 'y': np.array(y)}

def save_model(model, model_path):
    model.save(model_path)

