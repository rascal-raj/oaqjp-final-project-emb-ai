from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector


app = Flask("myapp")

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route('/emotionDetector')
def emot_detector():
    text_to_analyse = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyse)

    if response['dominant_emotion'] is None:
        return "invalid input"
    else:
        return (
            f"For the given statement, the system response is "
            f"'anger': {response['anger']}, " 
            f"'disgust': {response['disgust']}, "   
            f"'fear': {response['fear']}, "   
            f"'joy': {response['joy']}, and "   
            f"'sadness': {response['sadness']}. "   
            f"The dominant emotion is <b> {response['dominant_emotion']}<b>"   
        )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
