import os
import random
import time
from flask import Flask, Response
from prometheus_client import Counter, generate_latest


my_basic_counter = Counter(
    'my_basic_counter',
    'A basic counter.'
)
CONTENT_TYPE_LATEST = str('text/plain; version=0.0.4; charset=utf-8')
MAX_SLEEP = float(os.environ.get('MAX_SLEEP', 1.5))

app = Flask(__name__)

@app.route('/')
def hello():
    sleep_time = random.uniform(0, MAX_SLEEP)
    time.sleep(sleep_time)

    return "Slept for " + str(sleep_time)

@app.route('/metrics', methods=['GET'])
def get_data():
    """Returns all data as plaintext."""
    my_basic_counter.inc()
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)