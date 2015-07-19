from flask import render_template, send_file

from . import app, basedir

import os

@app.route('/')
def index():
    return render_template(
            'webapp.html',
    )

@app.route('/illuminati/<id>')
def illuminati(id):
    return send_file(
            os.path.join(
                basedir,
                app.config['ILLUMINATI_OUTPUT_DIR'],
                id + '.' + app.config['ILLUMINATI_FORMAT'],
            ),
            conditional=True,
    )
