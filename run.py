import os
import logging
from logging import Formatter, FileHandler

from app import app

BIN_PATH = os.path.join(os.getcwd(), 'bin')
os.environ["PATH"] += os.pathsep + BIN_PATH

@app.errorhandler(500)
def internal_error(error):
    return 500

@app.errorhandler(404)
def not_found_error(error):
    return 404

if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')


if __name__ == '__main__':
    app.run(debug=True, port=10101)
