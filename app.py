from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "DevSecOps test container running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)