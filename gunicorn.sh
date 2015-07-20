#!/bin/bash

exec gunicorn --preload -n illuminaticonfirmed -w 12 -k eventlet -b 127.0.0.1:7865 backend:app
