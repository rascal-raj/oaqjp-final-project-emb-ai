"""
This module provides the functionality for the server.
It handles the routes and communication for the application.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("myapp")

@app.route("/")
def render_index_page():
    """
    This function renders index.html    
    Parameters:
    None

    Returns:
    index.html
    """
    return render_template('index.html')

@app.route('/emotionDetector')
def emot_detector():
    """
    This function calls emotion detector and returns the formatted output.
    
    """
    text_to_analyse = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyse)

    if response['dominant_emotion'] is None:
        return "<b> Invalid text! Please try again! <b>"
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
