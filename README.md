## Description

This is a Flask application that's run using `docker-compose`.  It has a single endpoint: `/`

## Goal
Create a Prometheus alert that fires if a request to `/` takes longer than 1 second.  
You should use Prometheus's docker compose implementation found here: https://github.com/vegasbrianc/prometheus 
