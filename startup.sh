#!/bin/bash

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn api.wsgi:application \
    --bind 0.0.0.0:8081 \
    --workers 3