from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>My DevOps Project 2</h1>
    <p>Flask application running successfully!</p>
    <p>Built with Python, Docker, Jenkins and AWS.</p>
    """

@app.route("/health")
def health():
    return jsonify(status="healthy"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
