from flask import Flask
import requests
import os

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):

    url = os.environ.get("BASE_URL_FOR_PROXY") + "/" + path

    r = requests.get(url).text

    return r
