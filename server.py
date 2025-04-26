from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/emotionDetector')
def sentiment_analisys():
    text = request.args.get("textToAnalyze")

    analisys = emotion_detector(text)

    if analisys.get('dominant_emotion') == None:
        return 'Invalid text! Please try again!'

    return f"For the given statement, the system response is 'anger': {analisys.get('anger')}, \
    'disgust': {analisys.get('disgust')}, 'fear': {analisys.get('fear')}, \
    'joy': {analisys.get('joy')} and 'sadness': {analisys.get('sadness')}. \
    The dominant emotion is {analisys.get('dominant_emotion')}."
    