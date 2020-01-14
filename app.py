import time
import random
from flask import Flask, Response


app = Flask(__name__)


@app.route('/')
def hello():
    sleep_time = random.uniform(0, 1.5)
    time.sleep(sleep_time)

    return "Slept for " + str(sleep_time)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)