from flask import Flask, render_template, request
from EmotionDetection.emotion_detector import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emotion_detector():

    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion detector and store the response
    response = emotion_detector(text_to_analyze)

    # Extract individual emotion scores and dominant emotion
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Return a formatted string with scores
    return "For the given statement, the system response is 'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {}, and 'sadness': {}. The dominant emotion is {}.".format(anger, disgust, fear, joy, sadness, dominant_emotion)

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000)