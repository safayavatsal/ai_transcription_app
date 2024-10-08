import pyttsx3
import speech_recognition as sr
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/voice-to-text', methods=['POST'])
def voice_to_text():
    recognizer = sr.Recognizer()
    audio_file = request.files['audio']
    audio_data = sr.AudioFile(audio_file)
    with audio_data as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio, language="hi-IN")  # Hindi example
        return jsonify({"text": text})
    except sr.UnknownValueError:
        return jsonify({"error": "Unable to recognize speech"}), 400

@app.route('/text-to-voice', methods=['POST'])
def text_to_voice():
    data = request.get_json()
    text = data['text']
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    return jsonify({"message": "Text converted to speech"})

if __name__ == "__main__":
    app.run(debug=True)

