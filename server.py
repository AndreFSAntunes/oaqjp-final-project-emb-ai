"""Flask server for Emotion Detection application.

This module provides a web interface to input text
and detect emotions using the emotion_detector function.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    """
    Render the home page.

    Returns:
        str: The rendered HTML content of the index page.
    """
    return render_template('index.html')

@app.route('/emotionDetector')
def sentiment_analisys():
    """
    Analyze the sentiment of a given text input.

    If no dominant emotion is found, an error message is returned.

    Returns:
        str: A formatted analysis result or an error message.
    """
    text = request.args.get("textToAnalyze")

    analisys = emotion_detector(text)

    if analisys.get('dominant_emotion') is None:
        return 'Invalid text! Please try again!'

    return f"For the given statement, the system response is 'anger': {analisys.get('anger')}, \
    'disgust': {analisys.get('disgust')}, 'fear': {analisys.get('fear')}, \
    'joy': {analisys.get('joy')} and 'sadness': {analisys.get('sadness')}. \
    The dominant emotion is {analisys.get('dominant_emotion')}."
