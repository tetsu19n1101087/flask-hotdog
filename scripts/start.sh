#!/bin/bash

cd ~/flask-hotdog
sudo nginx -s reload
sudo gunicorn -b localhost:5000 test:app
