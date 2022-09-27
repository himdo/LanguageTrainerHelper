from transformers import GPTJForCausalLM
import torch
from transformers import AutoTokenizer

class GPT_J:
    def __init__(self):
        #Will need at least 13-14GB of Vram for CUDA
        if torch.cuda.is_available():
            print('GPU')
            self.model =  GPTJForCausalLM.from_pretrained("EleutherAI/gpt-j-6B", torch_dtype=torch.float16).cuda()
        else:
            print('CPU')
            self.model =  GPTJForCausalLM.from_pretrained("EleutherAI/gpt-j-6B", torch_dtype=torch.float16)

        self.tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-j-6B")
        self.model.eval()

    def GPTJ_GetResponse(self, data):
        # data:
        # {
        #   'prompt': 'this is a prompt, how are ',
        #   'max_length': 500,
        #   'top_p': 0.7,
        #   'top_k': 0,
        #   'temperature': 0.8,
        #   'do_sample': true
        # }
        input_text = data['prompt']
        input_ids = self.tokenizer.encode(str(input_text), return_tensors='pt').cuda()

        output = self.model.generate(
            input_ids,
            do_sample=data['do_sample'],
            max_length=data['max_length'],
            top_p=data['top_p'],
            top_k=data['top_k'],
            temperature=data['temperature'],
        )

        # print(self.tokenizer.decode(output[0], skip_special_tokens=True))
        return self.tokenizer.decode(output[0], skip_special_tokens=True)

    def Generate(self, data):
        # data:
        # {
        #   'prompt': 'this is a prompt, how are ',
        #   'max_length': 500,
        #   'top_p': 0.7,
        #   'top_k': 0,
        #   'temperature': 0.8,
        #   'do_sample': true
        # }
        return self.GPTJ_GetResponse(data)