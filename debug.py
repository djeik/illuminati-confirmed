#!/usr/bin/env python

from backend import app

if __name__ == '__main__':
    app.run(
            host='0.0.0.0',
            port=app.config['DEBUG_PORT'],
    )
