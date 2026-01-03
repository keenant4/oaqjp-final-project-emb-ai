"""
Flask server for the Emotion Detector web application.
Handles user input, calls the emotion detection function,
and returns formatted results or error messages.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def index():
    """
    Render the main HTML page for user input.
    """
    return render_template("index.html")

@app.route("/emotionDetector", methods=["POST"])
def emotion_detection():
    """
    Receive text from the user, run the emotion detector,
    and return a formatted response or an error message.
    """
    text_to_analyze = request.form.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (
    f"For the given statement, the system response is "
    f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
    f"'fear': {response['fear']}, 'joy': {response['joy']} and "
    f"'sadness': {response['sadness']}. The dominant emotion is "
    f"{response['dominant_emotion']}.",
    200
)

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
