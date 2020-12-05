import functools

from flask import url_for, render_template, Blueprint

bp = Blueprint("tts", __name__)

@bp.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@bp.route("/new", methods=("GET", "POST"))
def newTask():
    pass
