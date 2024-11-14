'''module responsible for querying the Watson NLP API'''
import requests

urlbase = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService'

'''function responsible for getting the emotion involved in a text passed by arguments'''
def emotion_detector(text_to_analyse):
    endpoint = '/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }
    x = requests.post(url = urlbase + endpoint, json = input_json, headers = headers)
    return x.text