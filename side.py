import requests
import os
from dotenv import load_dotenv

load_dotenv()
DeepAPI = os.getenv("DeepAPI")


def translate(text, target_lang):
    url = "https://api-free.deepl.com/v2/translate"
    data = {
        "auth_key": DeepAPI,
        "text": text,
        "target_lang": target_lang.upper()
    }

    response = requests.post(url, data=data)
    result = response.json()
    return result["translations"][0]["text"]
