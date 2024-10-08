import argparse
import os

import numpy as np
import tensorflow as tf
from model.asr_model import ASRModel  # Import your ASR model architecture
from utils import load_data, preprocess_data, save_model


def train_model(epochs, batch_size):
    # Load and preprocess data
    audio_files, transcriptions = load_data('data/audio_samples', 'data/transcriptions')
    processed_data = preprocess_data(audio_files, transcriptions)

    model = ASRModel()
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    model.fit(processed_data['X'], processed_data['y'], epochs=epochs, batch_size=batch_size)
    save_model(model, 'model/checkpoints/asr_model.h5')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Train ASR Model')
    parser.add_argument('--epochs', type=int, default=10, help='Number of epochs to train')
    parser.add_argument('--batch_size', type=int, default=32, help='Batch size for training')
    args = parser.parse_args()

    train_model(args.epochs, args.batch_size)

