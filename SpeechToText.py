import os
from Languages import Languages

class SpeechToText:
    # This is using whisper as the main model
    # For this to work you need to setup and install whisper to your system, see https://github.com/openai/whisper#setup

    def __init__(self, language=Languages.English):
        if language == Languages.Japanese:
            self.lang = 'Japanese'
        elif language == Languages.English:
            self.lang = 'English'
        elif language == Languages.Mandarin:
            self.lang = 'Chinese'
    
    # This returns a string or False if something went wrong
    def GenerateText(self, pathToFile):
        try:
            os.system('whisper ' + str(pathToFile) + ' --language ' + self.lang + ' --task translate')
            textPath = str(pathToFile) + '.txt'
            f = open(textPath, 'r', encoding="utf-8")
            fileContents = ""
            for x in f:
                fileContents += x
            f.close()
            # Cleanup whisper files
            os.remove(textPath)
            os.remove(str(pathToFile) + '.vtt')
            return x
        except:
            return False

# stt = SpeechToText(Languages.English)
# print(stt.GenerateText('./voice.wav'))