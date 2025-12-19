from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from AKS via GitHub Actions 🚀\n"

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

