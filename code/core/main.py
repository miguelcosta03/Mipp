from code.voice.speech_recognizer import SpeechRecognizer
from code.voice.text2speech import VoiceEngine

speechRecognizer = SpeechRecognizer()
voiceEngine = VoiceEngine()

keepTalking = True
while keepTalking:
    recognizedAudio = speechRecognizer.recognize()
    print(f'You said: {recognizedAudio}')
    if recognizedAudio == 'goodbye':
        print('Goodbye!')
        keepTalking = False
        break
