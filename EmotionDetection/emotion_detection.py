import requests

def emotion_detector (text_to_analyse):
   URL =  'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
   HEADERS =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
   myobj =  { "raw_document": { "text": text_to_analyse} }
   response = requests.post(URL, json = myobj, headers=HEADERS)
   response_data = response.json()
   emotions = response_data['emotionPredictions'][0]['emotion']

   anger_score = emotions['anger']
   disgust_score = emotions['disgust']
   fear_score = emotions['fear']
   joy_score = emotions['joy']
   sadness_score = emotions['sadness'] 

   dominant_emotion = max(emotions, key=emotions.get)

   formatted_output = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }

   return formatted_output