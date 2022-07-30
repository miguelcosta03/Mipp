import pyodbc


class Database:
    def __init__(self, driver, serverIP, databaseName, uid, pwd):
        self.driver = driver
        self.serverIP = serverIP
        self.databaseName = databaseName
        self.uid = uid
        self.pwd = pwd

        self.connection = pyodbc.connect(
            f"DRIVER={self.driver};"
            f"SERVER={self.serverIP};"
            f"DATABASE={self.databaseName};"
            f"UID={self.uid};"
            f"PWD={self.pwd}"
        )
        self.cursor = self.connection.cursor()

    def getSpeechID(self, userSpeech):
        query = f"""SELECT SpeechID FROM dbo.Speeches
                    WHERE UserSpeech='{userSpeech}';"""
        self.cursor.execute(query)
        speechID = str(self.cursor.fetchall()).replace('[', '').replace(']', '').replace('(', '').replace(')', '') \
            .replace("'", "").replace(',', '')
        return int(speechID)

    def getSpeechAnswer(self, speechID):
        query = f"""SELECT MippSpeech FROM dbo.Speeches
                    WHERE SpeechID={speechID}"""
        self.cursor.execute(query)
        speechAnswer = list(
            str(self.cursor.fetchall()).replace('[', '').replace(']', '').replace('(', '').replace(')', '') \
            .replace("'", "")
        )
        for popRound in range(0, 2):
            speechAnswer.pop(len(speechAnswer) - 1)

        formattedSpeechAnswer = ""
        for joinChar in speechAnswer:
            formattedSpeechAnswer += joinChar
        return formattedSpeechAnswer
