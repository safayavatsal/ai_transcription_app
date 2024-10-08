import os

import numpy as np
from model.tts_model import TTSModel
from utils import load_data, preprocess_data


def evaluate_model(model_path):
    model = tf.keras.models.load_model(model_path)
    text_samples, audio_clips = load_data('data/text_samples', 'data/audio_clips')
    processed_data = preprocess_data(text_samples, audio_clips)

    loss, mae = model.evaluate(processed_data['X'], processed_data['y'])
    print(f'Evaluation Loss: {loss:.4f}, Evaluation MAE: {mae:.4f}')

if __name__ == '__main__':
    evaluate_model('model/checkpoints/tts_model.h5')

