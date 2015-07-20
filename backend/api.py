from flask import request, jsonify, url_for

from . import app
from .confirm import confirm_illuminati
from tempfile import TemporaryFile

def json_die(message, code=400):
    response = jsonify(
            dict(
                message=message,
            ),
    )
    response.status_code = code
    return response

@app.route('/api/confirm', methods=['POST'])
def confirm():
    file = request.files['illuminati']
    if not file:
        return json_die(
                'No file submitted.',
                400,
        )

    s = file.read()
    tmp = TemporaryFile()
    tmp.write(s)
    tmp.seek(0)

    illuminati_id = confirm_illuminati(tmp)
    if not illuminati_id:
        return json_die(
                'Invalid file.',
                400,
        )

    return jsonify(
            dict(
                url=url_for('illuminati', id=illuminati_id),
                id=illuminati_id,
            ),
    )
