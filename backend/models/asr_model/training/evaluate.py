import os

import numpy as np
from model.asr_model import ASRModel
from utils import load_data, preprocess_data


def evaluate_model(model_path):
    model = tf.keras.models.load_model(model_path)
    audio_files, transcriptions = load_data('data/audio_samples', 'data/transcriptions')
    processed_data = preprocess_data(audio_files, transcriptions)

    loss, accuracy = model.evaluate(processed_data['X'], processed_data['y'])
    print(f'Evaluation Loss: {loss:.4f}, Evaluation Accuracy: {accuracy:.4f}')

if __name__ == '__main__':
    evaluate_model('model/checkpoints/asr_model.h5')

