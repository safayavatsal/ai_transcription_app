import os

import numpy as np


def load_data(data_dir):
    source_sentences = []
    target_sentences = []
    
    for filename in os.listdir(data_dir):
        if filename.endswith('.txt'):
            with open(os.path.join(data_dir, filename), 'r') as f:
                lines = f.readlines()
                for line in lines:
                    src, tgt = line.strip

