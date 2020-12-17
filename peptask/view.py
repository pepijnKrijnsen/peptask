import functools
from flask import url_for, render_template, Blueprint, request

from . import model


bp = Blueprint("view", __name__)

@bp.route("/", methods = ("GET", "POST"))
def index():
    if request.method == "POST":
        title = request.form["title"]
        due_date = request.form["duedate"]
        model.newTask(title, due_date)
    tasks = model.loadTasks()
    return render_template("index.html", tasks = tasks)


# @bp.route("/new", methods = ["POST"])
# def newTask():
#     title = request.form["title"]
#     due_date = request.form["due_date"]
#     model.newTask(title, due_date)
# 
# 
# @bp.route("/complete", methods=("GET", "POST"))
# def completeTask():
#     pass
