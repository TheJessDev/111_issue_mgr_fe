from flask import flask

app = Flask(__name__)

@app.get("/")
def ping():
    return {
        "status": "ok",
        "message": "pong - Hello world"
    }