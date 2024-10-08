class TranslationConfig:
    def __init__(self):
        self.input_vocab_size = 10000  # Source language vocabulary size
        self.target_vocab_size = 10000  # Target language vocabulary size
        self.embedding_dim = 256  # Dimension of embedding
        self.rnn_units = 512  # Units in the LSTM layers
        self.attention_units = 128  # Units in the attention mechanism
        self.learning_rate = 0.001  # Initial learning rate
        self.batch_size = 32  # Batch size for training
        self.epochs = 30  # Number of epochs

    def get_config(self):
        return {
            'input_vocab_size': self.input_vocab_size,
            'target_vocab_size': self.target_vocab_size,
            'embedding_dim': self.embedding_dim,
            'rnn_units': self.rnn_units,
            'attention_units': self.attention_units,
            'learning_rate': self.learning_rate,
            'batch_size': self.batch_size,
            'epochs': self.epochs
        }

# Example usage
translation_config = TranslationConfig()
print(translation_config.get_config())
