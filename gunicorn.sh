#!/bin/bash

exec gunicorn -n illuminaticonfirmed -b 127.0.0.1:7865 backend:app
