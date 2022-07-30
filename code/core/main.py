from code.voice.speech_recognizer import SpeechRecognizer
from code.voice.text2speech import VoiceEngine
from code.database.database import Database
from code.credentials.credentials import ServerCredentials

speechRecognizer = SpeechRecognizer()
voiceEngine = VoiceEngine()
database = Database(ServerCredentials.getServerDriver(), ServerCredentials.getServerIP(),
                    ServerCredentials.getDatabaseName(), ServerCredentials.getUID(),
                    ServerCredentials.getPassword())