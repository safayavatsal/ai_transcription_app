import os

import numpy as np
from model.translation_model import TranslationModel
from utils import load_data, preprocess_data


def evaluate_model(model_path):
    model = tf.keras.models.load_model(model_path)
    source_sentences, target_sentences = load_data('data/parallel_corpora')
    processed_data = preprocess_data(source_sentences, target_sentences)

    loss, accuracy = model.evaluate(processed_data['X'], processed_data['y'])
    print(f'Evaluation Loss: {loss:.4f}, Evaluation Accuracy: {accuracy:.4f}')

if __name__ == '__main__':
    evaluate_model('model/checkpoints/translation_model.h5')

