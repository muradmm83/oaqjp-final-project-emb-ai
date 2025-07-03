from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detection')

@app.route('/emotionDetector')
def analyze_emotion():
    text = request.args['textToAnalyze']
    response = emotion_detector(text)

    if response['dominant_emotion'] == None:
        return 'Invalid text!'
    return f"For the given statement, the system response is 'anger': {response['anger']}, 'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']}, 'sadness': {response['sadness']}. The dominant emotion is <b>{response['dominant_emotion']}</b>"

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)