import requests

class GPT_J_API:
    def __init__(self, url):
        self.url = url

    def Generate(self, data):
        response = requests.post(self.url, json=data)
        return response.text