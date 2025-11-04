from flask import Flask,jsonify
import random

app = Flask(__name__)
@app.route('/emoji')
def get_emoji():
    emojis = ['🤦‍♂️','🎶','😎','😜','💖','🤑','😵‍💫']
    return jsonify({'emoji': random.choice(emojis)})
if __name__ == '__main__':
    app.run(host= '0.0.0.0', port = 5001)