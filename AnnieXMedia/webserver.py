import os
from threading import Thread
from flask import Flask
from werkzeug.serving import make_server

web_app = Flask(__name__)

@web_app.get("/")
def health():
    return "AnnieXMedia is running", 200

@web_app.get("/health")
def health_check():
    return {"status": "ok"}, 200

def _serve():
    port = int(os.environ.get("PORT", "10000"))
    server = make_server("0.0.0.0", port, web_app)
    server.serve_forever()

def start_web_server():
    Thread(target=_serve, name="render-http", daemon=True).start()
