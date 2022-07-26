import speech_recognition as sr


class SpeechRecognizer:
    def __init__(self):
        recognizer = sr.Recognizer()
        self.recognizer = recognizer

    def recognize(self):
        with sr.Microphone() as microphone:
            print('Speak:')
            audio = self.recognizer.listen(microphone)
        try:
            return self.recognizer.recognize_google(audio, language="en")
        except sr.UnknownValueError:
            return False
