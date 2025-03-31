import torch
from TTS.api import TTS

# Define device (either 'cuda' if a GPU is available, or 'cpu' if not)
device = "cuda" if torch.cuda.is_available() else "cpu"

# Init TTS with the target model name
tts = TTS(model_name="tts_models/de/thorsten/tacotron2-DDC", progress_bar=False).to(device)

# Define output path for the generated audio file
OUTPUT_PATH = "output_es.wav"  # Change to Spanish output file name

# Run TTS
tts.tts_to_file(text="Soy un mensaje de prueba.", file_path=OUTPUT_PATH)

# Example voice cloning with YourTTS in Spanish
tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts", progress_bar=False).to(device)

# Generate speech with voice cloning in Spanish
tts.tts_to_file("Esto es clonación de voz.", speaker_wav="my/cloning/audio.wav", language="es", file_path="output_es_cloning.wav")

# Print the paths where files are saved
print(f"Speech saved to: {OUTPUT_PATH}")
