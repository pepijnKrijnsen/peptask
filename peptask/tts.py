import functools

from flask import url_for, render_template, Blueprint

bp = Blueprint("tts", __name__)

@bp.route("/", methods=["GET"])
def index():
    import os, json
    tasks = []
    dir = "peptask/tasks/active/"
    tasks_files = os.listdir(dir)
    for f in tasks_files:
        path = dir + f
        fo = open(path)
        task_data = fo.read(); fo.close()
        d = json.loads(task_data)
        tasks.append(d)
    return render_template("index.html", tasks = tasks)


@bp.route("/new", methods=("GET", "POST"))
def newTask():
    pass
