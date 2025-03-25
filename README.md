# Poly Language Learning Robot

## Set up
- python3 -m venv venv
- mac/linx: source venv/bin/activate
- mac/linux: brew install go
- windows: venv\Scripts\activate
- pip install pyaudio
- pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client google-cloud-speech
- cd speech_to_text
- put the poly_robot.json in the folder
- python3 demo1.py

## Run
- cd recorder
- python3 recorder.py
- move the audio.wav file into the speech_to_text folder
- cd ..
- cd speech_to_text
- python3 demo1.py
- cd ..
- cd free-translation-api (refer to https://github.com/ismalzikri/free-translate-api)
- go run main.go
- curl -X POST -H "Content-Type: application/json" -d '{"text": "Hello", "to": "de"}' http://localhost:8000/translate