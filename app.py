from flask import Flask, render_template, request
from gtts import gTTS

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    text = request.form['text']
    tts = gTTS(text)
    tts.save('static/output.mp3')
    return render_template('index.html', converted=True)

if __name__ == '__main__':
    app.run(debug=True)
