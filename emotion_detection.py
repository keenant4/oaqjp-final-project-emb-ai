import urllib.request
import json

def emotion_detector(text_to_analyse):
    URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    Headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    Input = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    req = urllib.request.Request(
        URL,
        data=json.dumps(Input).encode("utf-8"),
        headers=Headers,
        method="POST"
    )

    try:
        with urllib.request.urlopen(req) as response:
            response_data = response.read().decode("utf-8")
            formatted_response = json.loads(response_data)

            emotion_scores = formatted_response['emotionPredictions'][0]['emotion']
            dominant_emotion = max(emotion_scores, key=emotion_scores.get)

            return {
                'anger': emotion_scores['anger'],
                'disgust': emotion_scores['disgust'],
                'fear': emotion_scores['fear'],
                'joy': emotion_scores['joy'],
                'sadness': emotion_scores['sadness'],
                'dominant_emotion': dominant_emotion
            }

    except urllib.error.HTTPError:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
