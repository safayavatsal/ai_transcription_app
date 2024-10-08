class ASRConfig:
    def __init__(self):
        self.vocab_size = 1000  # Size of the vocabulary
        self.input_dim = 64  # Input features dimension (MFCC, spectrogram, etc.)
        self.rnn_units = 128  # Units in the LSTM layers
        self.attention_units = 64  # Units in the attention mechanism
        self.learning_rate = 0.001  # Initial learning rate
        self.batch_size = 32  # Batch size for training
        self.epochs = 10  # Number of epochs

    def get_config(self):
        return {
            'vocab_size': self.vocab_size,
            'input_dim': self.input_dim,
            'rnn_units': self.rnn_units,
            'attention_units': self.attention_units,
            'learning_rate': self.learning_rate,
            'batch_size': self.batch_size,
            'epochs': self.epochs
        }

# Example of accessing the config
asr_config = ASRConfig()
print(asr_config.get_config())
