# Poly Language Learning Robot

## Set up
- python3.9 -m venv venv
- mac/linx: source venv/bin/activate
- windows: venv\Scripts\activate
- pip install pyaudio TTS torch
- cd speech_to_text
- put the poly_robot.json in the folder
- pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client google-cloud-speech

## Run
- cd speech to text
- go run main.go to start hosting translation server
- open new terminal
- run python3 speech_to_text.py