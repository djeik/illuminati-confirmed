from . import app, basedir

import subprocess as sp
import random
from os import path

def confirm_illuminati(handle):
    """ Confirms the illuminati on the image represented by a file handle.

    Spawns the `confirmer.py` script with Python 2 and writes the data of the
    supplied file handle into its stdin. `confirmer.py` will write its output
    to a file with a random name in the `output` directory.

    The random file name (not the full path!) is returned.
    """
    id = ''.join(
            [
                random.choice(
                    app.config[
                        'RANDOM_CHARS'
                    ],
                )
                for _
                in range(
                    app.config[
                        'FILENAME_LENGTH'
                    ],
                )
            ],
    )
    filename = id + '.' + app.config['ILLUMINATI_FORMAT']

    output_path = path.join(
            basedir,
            app.config['ILLUMINATI_OUTPUT_DIR'],
            filename,
    )

    script_path = path.join(
            basedir,
            app.config['SCRIPTS_DIR'],
            'confirmer.py',
    )

    try:
        with open('/dev/null') as DEVNULL:
            sp.check_call(
                    [
                        script_path,
                        output_path,
                    ],
                    stdin=handle,
                    stdout=DEVNULL,
                    stderr=DEVNULL,
            )
    except sp.CalledProcessError:
        return None

    return id
