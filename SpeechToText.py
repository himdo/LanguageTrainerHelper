import whisper
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
        
        self.model = whisper.load_model("large")
        
    
    # This returns a string or False if something went wrong
    def GenerateText(self, path):
        try:
            audio = whisper.load_audio(path)
            audio = whisper.pad_or_trim(audio)
            
            mel = whisper.log_mel_spectrogram(audio).to(self.model.device)
            
            _, probs = self.model.detect_language(mel)
            # task = transcribe or translate
            options = whisper.DecodingOptions(fp16 = False, language=self.lang, task='translate')
            result = whisper.decode(self.model, mel, options)
            
            return result.text
        except:
            return False

# if __name__ == '__main__':
#     from datetime import datetime
#     start = datetime.now()
#     stt = SpeechToText(Languages.Japanese)
#     print(stt.GenerateText('./a.wav'))
#     finished = datetime.now()
#     delta = finished - start
#     print(str(delta.total_seconds()))