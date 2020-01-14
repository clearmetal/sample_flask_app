import os
import random
import time
from flask import Flask, Response


app = Flask(__name__)

MAX_SLEEP = float(os.environ.get('MAX_SLEEP', 1.5))

@app.route('/')
def hello():
    sleep_time = random.uniform(0, MAX_SLEEP)
    time.sleep(sleep_time)

    return "Slept for " + str(sleep_time)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)