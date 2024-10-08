import argparse
import os

import numpy as np
import tensorflow as tf
from model.tts_model import TTSModel  # Import your TTS model architecture
from utils import load_data, preprocess_data, save_model


def train_model(epochs, batch_size):
    # Load and preprocess data
    text_samples, audio_clips = load_data('data/text_samples', 'data/audio_clips')
    processed_data = preprocess_data(text_samples, audio_clips)

    model = TTSModel()
    model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])

    model.fit(processed_data['X'], processed_data['y'], epochs=epochs, batch_size=batch_size)
    save_model(model, 'model/checkpoints/tts_model.h5')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Train TTS Model')
    parser.add_argument('--epochs', type=int, default=10, help='Number of epochs to train')
    parser.add_argument('--batch_size', type=int, default=32, help='Batch size for training')
    args = parser.parse_args()

    train_model(args.epochs, args.batch_size)

