'''module responsible for querying the Watson NLP API'''
import requests, json

urlbase = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService'

'''function responsible for getting the emotion involved in a text passed by arguments'''
def emotion_detector(text_to_analyse):
    endpoint = '/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url = urlbase + endpoint, json = input_json, headers = headers)
    emotionsList = json.loads(response.text)['emotionPredictions'][0]['emotion']

    dominant_emotion = ''
    dominant_value = 0
    result = {}

    for em_key in emotionsList:        
        result[em_key] = emotionsList[em_key]
        if emotionsList[em_key] >= dominant_value:
            dominant_emotion = em_key
            dominant_value = emotionsList[em_key]
    result["dominant_emotion"] = dominant_emotion 

    return json.dumps(result, indent = 4)
