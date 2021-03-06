import os
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello ' + os.environ['USER_NAME'] + ' from a Container!'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=False)
