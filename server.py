from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app=Flask("Emotion Detector")

@app.route('/emotionDetector')
def emotion_detection():
    text_to_analyze = request.args.get('textToAnalyze')
    response=emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "invalid input! "
    return ("For the given statement, the system response is anger: {}, disgust: {}, fear: {}, joy: {} and sadness:{}, The dominant emotion is {} ".format(response['anger'],response['disgust'],response['fear'],response['joy'],response['sadness'],response['dominant_emotion'] ),200 )

@app.route('/')
def index():

    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)