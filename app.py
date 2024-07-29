from flask import Flask, render_template, request, jsonify
from sentiment_analysis import sentiment_analyzer

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/api/sentiment', methods=['POST'])
def sentiment_analysis():
    try:
        data = request.get_json()
        if not data:
            raise ValueError("No data provided to perform sentiment analysis")
    except Exception as e:
        return jsonify({"error": "No text provided to perform sentiment analysis"}), 400

    text = data.get("text")

    if text:
        result = sentiment_analyzer(text=text)
        return jsonify({**result, "text": text}), 200
    else:
        return jsonify({"error": "No text provided"}), 400


if __name__ == '__main__':
    app.run(debug=True)
