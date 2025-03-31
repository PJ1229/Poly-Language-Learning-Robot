import io
import pyaudio
import wave
import requests
import json
from google.oauth2 import service_account
from google.cloud import speech
from dataclasses import dataclass, asdict

@dataclass
class StreamParams:
    format: int = pyaudio.paInt16
    channels: int = 1
    rate: int = 44100
    frames_per_buffer: int = 1024
    input: bool = True
    output: bool = False

    def to_dict(self) -> dict:
        return asdict(self)

class Recorder:
    def __init__(self, stream_params: StreamParams) -> None:
        self.stream_params = stream_params
        self._pyaudio = None
        self._stream = None
        self._wav_file = None

    def record(self, duration: int, save_path: str) -> None:
        print("Start recording...")
        self._create_recording_resources(save_path)
        self._write_wav_file_reading_from_stream(duration)
        self._close_recording_resources()
        print("Stop recording.")

    def _create_recording_resources(self, save_path: str) -> None:
        self._pyaudio = pyaudio.PyAudio()
        self._stream = self._pyaudio.open(**self.stream_params.to_dict())
        self._create_wav_file(save_path)

    def _create_wav_file(self, save_path: str) -> None:
        self._wav_file = wave.open(save_path, 'wb')
        self._wav_file.setnchannels(self.stream_params.channels)
        self._wav_file.setsampwidth(self._pyaudio.get_sample_size(self.stream_params.format))
        self._wav_file.setframerate(self.stream_params.rate)

    def _write_wav_file_reading_from_stream(self, duration: int) -> None:
        for _ in range(int(self.stream_params.rate / self.stream_params.frames_per_buffer * duration)):
            audio_data = self._stream.read(self.stream_params.frames_per_buffer)
            self._wav_file.writeframes(audio_data)

    def _close_recording_resources(self) -> None:
        self._wav_file.close()
        self._stream.close()
        self._pyaudio.terminate()

# Speech-to-Text Processing
def transcribe_audio(audio_file: str, client_file: str):
    credentials = service_account.Credentials.from_service_account_file(client_file)
    client = speech.SpeechClient(credentials=credentials)

    with io.open(audio_file, 'rb') as f:
        content = f.read()
        audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
        language_code='en-US'
    )

    response = client.recognize(config=config, audio=audio)

    transcript = ""
    for result in response.results:
        transcript += result.alternatives[0].transcript + " "
    
    return transcript.strip()

# Translation Processing
def translate_text(text: str, target_language: str):
    url = "http://localhost:8000/translate"
    payload = {"text": text, "to": target_language}
    headers = {"Content-Type": "application/json"}
    
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    
    if response.status_code == 200:
        translated_text = response.json().get("translatedText", "")
        return translated_text
    else:
        print("Translation failed:", response.text)
        return ""

if __name__ == "__main__":
    stream_params = StreamParams()
    recorder = Recorder(stream_params)
    audio_path = "audio.wav"
    service_account_file = "poly_robot.json"
    
    recorder.record(5, audio_path)
    transcript = transcribe_audio(audio_path, service_account_file)
    print("Transcript:", transcript)
    
    translated_text = translate_text(transcript, "es")
    print("Translated Text:", translated_text)
