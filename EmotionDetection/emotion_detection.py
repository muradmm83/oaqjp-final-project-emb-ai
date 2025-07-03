import requests, json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json=input, headers=headers)

    if response.status_code == 400:
        result = {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}
    else:
        formatted_response = json.loads(response.text)
        data = formatted_response['emotionPredictions'][0]['emotion']
        result = {
            'anger': data['anger'],
            'disgust': data['disgust'],
            'fear': data['fear'],
            'joy': data['joy'],
            'sadness': data['sadness']
        }

        dominant_emotion = max(result, key=result.get)
        result['dominant_emotion'] = dominant_emotion
    
    return result
