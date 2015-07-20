from flask import render_template, send_file, abort

from . import app, basedir

import os

def illuminati_path(id):
    return os.path.join(
            basedir,
            app.config['ILLUMINATI_OUTPUT_DIR'],
            id + '.' + app.config['ILLUMINATI_FORMAT'],
    )

@app.route('/')
def index():
    return render_template(
            'webapp.html',
    )

@app.route('/illuminati/<id>')
def illuminati(id):
    path = illuminati_path(id)

    if not os.path.exists(path):
        abort(400)

    return send_file(
            path,
            conditional=True,
    )

@app.route('/<id>')
def illuminati_page(id):
    return render_template(
            'illuminati.html',
            id=id,
    )
