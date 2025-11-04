from flask import Flask
import random
import requests


app = Flask(__name__)

@app.route('/chiste')

def get_chiste():
    chistes = ["¿Que le dice un pez a otro? ¡Nada!",
               "¿Porque los pajaros no ocupan Facebook? ¡Porque usan Twitter!",
               "¿Que le dice un moai a otro moai? No te moai"]
    chiste_elegido =random.choice(chistes)
    try:
        
        response_emoji = requests.get("http//servicio-emojis:5001/emoji")
        emoji = response_emoji.json()['emoji']
    except requests.exceptions.ConnectionError:
        emoji = "😒"
        
    return f"<h1>{chiste_elegido}{emoji}</h1>"
if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000)