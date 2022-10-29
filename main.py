from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"slackUsername": "mileba", "backend": True, "age": 24, "bio": "I am a web3 enthusiast"})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
