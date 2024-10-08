# Use a base image with Python 3.9
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements.txt files for ASR, TTS, and Translation
COPY asr_model/requirements.txt ./asr_model/
COPY tts_model/requirements.txt ./tts_model/
COPY translation_model/requirements.txt ./translation_model/

# Install system dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libsndfile1 \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r ./asr_model/requirements.txt \
    && pip install --no-cache-dir -r ./tts_model/requirements.txt \
    && pip install --no-cache-dir -r ./translation_model/requirements.txt

# Copy the application code
COPY . .

# Expose necessary ports (modify as needed)
# Example for Flask or FastAPI
EXPOSE 5000  

# Command to run your application (update as needed)
CMD ["python", "your_main_application.py"]
