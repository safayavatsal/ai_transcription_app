import os
import argparse
import numpy as np
import tensorflow as tf
from model.translation_model import TranslationModel  # Import your translation model architecture
from utils import load_data, preprocess_data, save_model

def train_model(epochs, batch_size):
    # Load and preprocess data
    source_sentences, target_sentences = load_data('data/parallel_corpora')
    processed_data = preprocess_data(source_sentences, target_sentences)

    model = TranslationModel()
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    model.fit(processed_data['X'], processed_data['y'], epochs=epochs, batch_size=batch_size)
    save_model(model, 'model/checkpoints/translation_model.h5')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Train Translation Model')
    parser.add_argument('--epochs', type=int, default=10, help='Number of epochs to train')
    parser.add_argument('--batch_size', type=int, default=32, help='Batch size for training')
    args = parser.parse_args()

    train_model(args.epochs, args.batch_size)

