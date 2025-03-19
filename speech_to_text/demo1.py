import io
from google.oauth2 import service_account
from google.cloud import speech

# Path to your service account file
client_file = 'poly_robot.json'

# Create credentials using the service account file
credentials = service_account.Credentials.from_service_account_file(client_file)

# Initialize the speech client
client = speech.SpeechClient(credentials=credentials)

# Path to the new mono audio file
audio_file = 'audio_sample_mono.wav'

# Read the audio file into memory
with io.open(audio_file, 'rb') as f:
    content = f.read()
    audio = speech.RecognitionAudio(content=content)

# Configure recognition settings
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=48000,  # Adjust to your file's sample rate
    language_code='en-US'
)

# Call the API to recognize the speech in the audio file
response = client.recognize(config=config, audio=audio)

# Print the recognition results
for result in response.results:
    print('Transcript:', result.alternatives[0].transcript)
