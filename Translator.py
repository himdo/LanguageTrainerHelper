from transformers import pipeline
# Currently only En to Ja works

class Translator:
    def __init__(self):
        # https://huggingface.co/staka/fugumt-en-ja
        # en to jp BLEU(1*) 32.7
        self.fugu_translator = pipeline('translation', model='staka/fugumt-en-ja')

    def translate(self, sentence):
        return self.fugu_translator(sentence)[0]['translation_text']

# translator = Translator()
# print(translator.translate('Hello my name is John.'))