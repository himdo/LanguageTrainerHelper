import os

class SpeechToText:
    # This is using whisper as the main model
    # For this to work you need to setup and install whisper to your system, see https://github.com/openai/whisper#setup

    def __init__(self):
        self.lang = 'English'
    
    # This returns a string or False if something went wrong
    def GenerateText(self, pathToFile):
        try:
            os.system('whisper ' + str(pathToFile) + ' --language ' + self.lang)
            textPath = str(pathToFile) + '.txt'
            f = open(textPath)
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

# stt = SpeechToText()
# print(stt.GenerateText('./jfk.flac'))