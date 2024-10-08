import sentencepiece as spm

def tokenize_text(text, model_path):
    sp = spm.SentencePieceProcessor()
    sp.load(model_path)
    return sp.encode_as_pieces(text)

# Example usage:
# tokens = tokenize_text("Hello, world!", '/path/to/spm_model.model')
