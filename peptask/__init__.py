import os
from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config = True)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app