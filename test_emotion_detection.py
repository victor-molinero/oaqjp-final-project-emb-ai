import unittest, json
from myUtils import CustomDecoder

from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test1(self):
        dominant_emotion = json.loads(emotion_detector("I am glad this happened"))["dominant_emotion"]
        self.assertEqual(dominant_emotion,"joy")
        dominant_emotion = json.loads(emotion_detector("I am really mad about this"))["dominant_emotion"]
        self.assertEqual(dominant_emotion,"anger")
        dominant_emotion = json.loads(emotion_detector("I feel disgusted just hearing about thi"))["dominant_emotion"]
        self.assertEqual(dominant_emotion,"disgust")
        dominant_emotion = json.loads(emotion_detector("I am so sad about this"))["dominant_emotion"]
        self.assertEqual(dominant_emotion,"sadness")
        dominant_emotion = json.loads(emotion_detector("I am really afraid that this will happen"))["dominant_emotion"]
        self.assertEqual(dominant_emotion,"fear")        
unittest.main()