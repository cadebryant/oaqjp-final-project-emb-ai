"""
Web server for the emotion detector application.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    """
    Calls the emotion detector function in the EmotionDetection package
    in response to submitting the text to analyze in the Web app.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    emotions = emotion_detector(text_to_analyze)
    anger_score = emotions["anger"]
    disgust_score = emotions["disgust"]
    fear_score = emotions["fear"]
    joy_score = emotions["joy"]
    sadness_score = emotions["sadness"]
    dominant_emotion = emotions["dominant_emotion"]

    if dominant_emotion is None:
        return "Invalid text! Please try again!."

    result = ("For the given statement, the system response is " +
    f"'anger': {anger_score}, " +
    f"'disgust': {disgust_score}, " +
    f"'fear': {fear_score}, " +
    f"'joy': {joy_score} and " +
    f"'sadness': {sadness_score}. " +
    f"The dominant emotion is {dominant_emotion}.")

    return result

@app.route("/")
def render_index_page():
    """
    Renders the main page on which the emotion detection runs
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
