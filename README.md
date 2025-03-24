# Poly Language Learning Robot

## Set up
- python3 -m venv venv
- mac/linx: source venv/bin/activate
- windows: venv\Scripts\activate
- pip install pyaudio
- cd recorder
- cd ..
- cd speech_to_text
- put the poly_robot.json in the folder
- pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client google-cloud-speech
- python3 demo1.py

## Run
- cd recorder
- python3 recorder.py
- move the audio.wav file into the speech_to_text folder
- cd ..
- cd speech_to_text
- python3 demo1.py