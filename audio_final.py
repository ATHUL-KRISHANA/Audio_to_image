from flask import Flask, render_template, request, jsonify, send_file
import pyaudio
import speech_recognition as sr
from PIL import Image
from io import BytesIO
import requests
import base64

app = Flask(__name__)

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000

def record_audio(duration=10):
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    print("Recording...")
    frames = []

    for _ in range(0, int(RATE / CHUNK * duration)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Finished recording.")
    stream.stop_stream()
    stream.close()
    p.terminate()

    return b''.join(frames)

def recognize_speech(audio_data):
    recognizer = sr.Recognizer()
    audio = sr.AudioData(audio_data, RATE, 2)
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError as e:
        return f"Could not request results from Google API; {e}"

def get_image_from_colab(text):
    colab_url = "https://f28c-34-82-106-246.ngrok-free.app/generate_image"  #
    response = requests.post(colab_url, data={'text': text})
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        
        img_io = BytesIO()
        image.save(img_io, 'JPEG')
        img_io.seek(0)
        img_base64 = base64.b64encode(img_io.read()).decode('utf-8')
        return img_base64
    else:
        return None

@app.route('/')
def index():
    return render_template('sam.html')

@app.route('/record', methods=['POST'])
def record():
    audio_data = record_audio()  
    recognized_text = recognize_speech(audio_data)
    if recognized_text:
        img_base64 = get_image_from_colab(recognized_text)
        if img_base64:
            return jsonify({"text": recognized_text, "image": img_base64})
        else:
            return jsonify({"error": "Failed to retrieve image from Colab"})
    else:
        return jsonify({"error": "Failed to recognize any text"})

if __name__ == '__main__':
    app.run(debug=True, port=8003)
