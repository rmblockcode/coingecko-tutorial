import requests
import os

TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')

def tel_send_message(text):
    TOKEN = TELEGRAM_TOKEN
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
        'chat_id': CHAT_ID,
        'text': text
        }
   
    r = requests.post(url,json=payload)
    print(r.content)
    return r