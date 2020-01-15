## Description

This is a Flask application that's run using `docker-compose`.  It has a single endpoint: `/`

## Goal
Create a Prometheus alert that fires if a request to `/` takes longer than 1 second.  
You should use Prometheus's docker compose implementation found here: https://github.com/vegasbrianc/prometheus 

# Solution
* See the updates to `app.py` and `requirements.txt`
* In the prometheus project, create the following alert in `prometheus/alert.rules`

```
- alert: TestHighRequestLatencyNew
    expr: request_latency_gauge_seconds > 1
    annotations:
      summary: "High request latency on {{ $labels.instance }}"
      description: "{{ $labels.instance }} has a median request latency above 1s (current value: {{ $value }}s)"
```
