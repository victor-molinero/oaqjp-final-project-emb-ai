"""
module resposible to render
"""
import json
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
from myUtils import CustomDecoder
app = Flask(__name__)

@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_app():
    """
    functions responsible to handle requests to calculate the emotion of user input
    """
    query = request.args.get('textToAnalyze')
    output = ""
    result = json.loads(emotion_detector(query), cls=CustomDecoder)

    if result['dominant_emotion'] is None:
        return 'Invalid text! Please try again!.'

    output = "For the given statement, the system response is "
    for dictkey in result:
        if dictkey != "dominant_emotion":
            output += f"'{dictkey}': {result[dictkey]}, "
    output += f". The dominant emotion is {result['dominant_emotion']}"

    return output

@app.route('/')
def render_index_page():
    """
    functions responsible for rendering main page of application
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
