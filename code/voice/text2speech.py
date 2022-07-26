import pyttsx3


class VoiceEngine:
    def __init__(self):
        engine = pyttsx3.Engine()
        self.engine = engine

    def getSpeakRate(self):
        return self.engine.getProperty('rate')

    def getSpeakVolume(self):
        return self.engine.getProperty('volume')

    def getSpeakVoice(self):
        return self.engine.getProperty('voice')

    def setSpeakRate(self, newRate):
        try:
            int(newRate)
            self.engine.setProperty('rate', newRate)
            print(f'New speak rate defined to: {newRate}.')
            return
        except ValueError:
            print('Invalid speak rate.')
            return

    def setSpeakVolume(self, newVolume):
        try:
            float(newVolume)
            self.engine.setProperty('volume', newVolume)
            print(f'New speak volume defined to: {newVolume}.')
            return
        except ValueError:
            print('Invalid speak volume.')
            return

    def setSpeakVoice(self, newVoice):
        try:
            int(newVoice)
            voices = self.engine.getProperty('voices')
            self.engine.setProperty('voice', voices[newVoice].id)
            if newVoice == 0:
                print('New speak voice defined to male.')
            elif newVoice == 1:
                print('New speak voice defined to female.')
            else:
                print('Invalid speak voice.')
            return
        except ValueError:
            print('Invalid speak voice.')
            return

    def speak(self, data):
        self.engine.say(data)
        self.engine.runAndWait()
