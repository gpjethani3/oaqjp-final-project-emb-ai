"""
Flask server configuration for the Watson NLP Emotion Detection application.
"""
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

# Initialize the Flask application
app = Flask(__name__)


@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Endpoint to analyze text and return the formatted emotion metrics.
    Handles blank inputs or 400 Bad Request outputs gracefully.
    """
    # Retrieve the text to analyze from the incoming request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Execute the emotion detection function
    response_data = emotion_detector(text_to_analyze)

    # Error Handling: Check if the dominant emotion is None
    if response_data['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Check for underlying system/network server errors
    if "error" in response_data:
        return f"System Error: {response_data['error']}"

    # Construct the successful response string format
    output_string = (
        f"For the given statement, the system response is "
        f"'anger': {response_data['anger']}, "
        f"'disgust': {response_data['disgust']}, "
        f"'fear': {response_data['fear']}, "
        f"'joy': {response_data['joy']} and "
        f"'sadness': {response_data['sadness']}. "
        f"The dominant emotion is {response_data['dominant_emotion']}."
    )

    return output_string


@app.route("/")
def render_index_page():
    """Renders the main application user interface."""
    return render_template('index.html')


if __name__ == "__main__":
    # Start the server on port 5000 with debug enabled for live reloads
    app.run(host="0.0.0.0", port=5000, debug=True)
