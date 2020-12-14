import functools
from flask import url_for, render_template, Blueprint

from . import model


bp = Blueprint("view", __name__)

@bp.route("/", methods=("GET", "POST"))
def index():
    if method == "POST":
        model.newTask(title, due_date)
    tasks = model.loadTasks()
    return render_template("index.html", tasks = tasks)


@bp.route("/new", methods=("GET", "POST"))
def newTask():
    pass


@bp.route("/complete", methods=("GET", "POST"))
def completeTask():
    pass
