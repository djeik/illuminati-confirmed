#!/usr/bin/env python

from backend import app

if __name__ == '__main__':
    app.run(
            debug=True,
            host='0.0.0.0',
            port=6500,
    )