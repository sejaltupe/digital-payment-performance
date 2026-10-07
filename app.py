from flask import Flask, jsonify
import time

app = Flask(__name__)


@app.route("/")
def home():
    return "Digital Payment Application is running!"


@app.route("/payment")
def payment():
    time.sleep(0.1)

    return jsonify({
        "status": "success",
        "message": "Payment processed successfully"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)