import functools
from flask import url_for, render_template, Blueprint, request, redirect

from . import model


bp = Blueprint("view", __name__)

@bp.route("/", methods = ("GET", "POST"))
def index():
    if request.method == "POST":
        title = request.form["title"]
        due_date = request.form["duedate"]
        res = model.newTask(title, due_date)
        if res != 0:
            return(res)
    tasks = model.loadTasks()
    return render_template("index.html", tasks = tasks)


@bp.route("/complete/<int:id>")
def completeTask(id):
    model.completeTask(id)
    return redirect("/")
