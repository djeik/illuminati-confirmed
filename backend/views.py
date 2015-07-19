from flask import render_template
from . import app

@app.route('/')
def index():
    return render_template(
            'webapp.html',
    )

@app.route('/img/<img_id>')
def get_img(img_id):
    abort(404)
