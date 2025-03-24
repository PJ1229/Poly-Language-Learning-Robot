from dataclasses import dataclass, asdict  # <-- Add asdict import
import pyaudio
import wave  # <-- Add wave module import

@dataclass
class StreamParams:
    format: int = pyaudio.paInt16
    channels: int = 1  # Changed from 2 to 1
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
        self._wav_file = wave.open(save_path, 'wb')  # <-- Ensure wave module is imported
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

if __name__ == "__main__":
    stream_params = StreamParams()
    recorder = Recorder(stream_params)
    recorder.record(5, "audio.wav")
