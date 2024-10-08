import librosa

def extract_mel_spectrogram(audio_path):
    y, sr = librosa.load(audio_path, sr=22050)
    mel_spec = librosa.feature.melspectrogram(y, sr=sr, n_mels=80)
    return mel_spec

# Example usage:
# mel_spec = extract_mel_spectrogram('/path/to/audio.wav')
