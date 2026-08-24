#!/bin/bash -e

pip install -e .

gunicorn --config gunicorn_dev_config.py 'dummy_app:init_app()'
