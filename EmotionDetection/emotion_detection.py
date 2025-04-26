import requests

def emotion_detector(text_to_analyse):

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, headers=headers, json=input_json)

    data = response.json()

    if response.status_code == 400:

        invalid_text = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

        return invalid_text


    anger_score = data["emotionPredictions"][0]["emotion"]["anger"]
    disgust_score = data["emotionPredictions"][0]["emotion"]["disgust"]
    fear_score = data["emotionPredictions"][0]["emotion"]["fear"]
    joy_score = data["emotionPredictions"][0]["emotion"]["joy"]
    sadness_score = data["emotionPredictions"][0]["emotion"]["sadness"]

    result = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
    }

    dominant_emotion = max(result, key=result.get)
    
    result["dominant_emotion"] = dominant_emotion

    return result

import json

if __name__ == "__main__":
    test_text = "I am very happy to test this method!"
    result = emotion_detector(test_text)
    print(result) # json.dumps(result, indent=4)