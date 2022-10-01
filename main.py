


from GPT_J import GPT_J
from GPT_J_API import GPT_J_API
from Languages import Languages
from MicrophoneRecorder import Microphone
from SpeechToText import SpeechToText
from TextToSpeech import TextToSpeech
from Translator import Translator
from PlayAudio import PlayAudio

class MainClass:
    def __init__(self):
        # self.GPT_J = GPT_J()
        self.GPT_J = GPT_J_API('http://localhost:5000/')
        # self.SpeechToText = SpeechToText(Languages.English)
        self.TextToSpeech = TextToSpeech(Languages.English)
        # # For this first test I won't use the translator
        # self.Translator = Translator()

        # self.Recorder = Microphone()
        print('Init Done')

    def main(self):
        conversation = []
        trueTextOriginal = """
\tThe following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.

\tHuman: Hello, who are you?
\tAI: I am an AI created by OpenAI. How can I help you today?\n""" 
        while True:
            trueText = trueTextOriginal
            text = input("Human: ")
            conversation.append(text)
            # trueText = 'The following is a conversation between a human and an AI chatbot.  The chatbot is a sport psychologist who specializes in people who are struggling with overthinking their role on a team which eventually sabotages their output. The chatbot will provide psychological science-based advice to help its patients to become better.\nHuman: ' + text + '\nAI Doctor: '
            
            for i in range(len(conversation)):
                if (i % 2 == 0):
                    trueText += "\tHuman: " + conversation[i] + "\n"
                else:
                    trueText += "\tAI: " + conversation[i] + "\n"

            # print('0000000000000000000000')
            # print(len(trueText))
            # print('0000000000000000000000')
            # print(trueText)
            # print('0000000000000000000000')

            gptData = {
                'prompt': trueText,
                'max_length': (int) (len(trueText)/3) + 100, # This pretty much makes sure to only generate 1 to 2 sentence more then whats needed
                'top_p': 0.7,
                'top_k': 0,
                'temperature': 0.8,
                'do_sample': True
            }
            response = self.GPT_J.Generate(gptData)
            # print('=======')
            # print(response)
            # print('=======')
            # print(len(conversation))
            
            # This gets the response that we are wanting from the AI that is the most recent 
            response = response.split('Human:')[1+(int)((len(conversation) + 1)/2)].split('AI:')[1].strip()
            # print('!!!!!')
            self.TextToSpeech.Generate(text=response, outputDir='voice.wav')
            print("AI: " + response)
            PlayAudio.play('voice.wav')
            # print('!!!!!')

            conversation.append(response)



def mainProgram():
    main = MainClass()
    main.main()


if __name__ == '__main__':
    mainProgram()