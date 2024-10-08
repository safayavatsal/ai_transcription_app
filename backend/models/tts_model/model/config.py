class TTSConfig:
    def __init__(self):
        self.vocab_size = 1000  # Size of vocabulary
        self.embedding_dim = 256  # Dimension of text embedding
        self.rnn_units = 512  # Units in the LSTM layers
        self.attention_units = 128  # Units in the attention mechanism
        self.learning_rate = 0.001  # Initial learning rate
        self.batch_size = 32  # Batch size for training
        self.epochs = 20  # Number of epochs

    def get_config(self):
        return {
            'vocab_size': self.vocab_size,
            'embedding_dim': self.embedding_dim,
            'rnn_units': self.rnn_units,
            'attention_units': self.attention_units,
            'learning_rate': self.learning_rate,
            'batch_size': self.batch_size,
            'epochs': self.epochs
        }

# Example usage
tts_config = TTSConfig()
print(tts_config.get_config())
