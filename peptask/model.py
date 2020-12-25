import os, json
from datetime import datetime, timedelta


def newTask(title, due_date):
    # data validation
    list_of_title_words = title.split()
    for word in list_of_title_words:
        if not word.isalnum():
            error = "Title must be alpha-numeric."
            return error
    try:
        int(due_date)
    except ValueError:
        due_date = renderWrittenDuedate(due_date)
        if due_date == 0:
            error = "Due date format not valid."
            return error
    fmnow = datetime.now().strftime("%Y%m%d")
    if due_date < fmnow:
        error = "Due date cannot be in the past."
        return error

    # get the latest unique id
    l = open("peptask/tasks/_latest")
    last_unique = int(l.read()); l.close()
    last_unique += 1
    last_unique = str(last_unique)
    l = open("peptask/tasks/_latest", "w")
    l.write(last_unique); l.close()

    # writing the file
    new_task_file = '{ "id": "%s", "title": "%s", "due_by": "%s" }' % (last_unique, title, due_date)
    nt = open("peptask/tasks/active/{}".format(last_unique), "x")
    nt.write(new_task_file); nt.close()
    return 0

def renderWrittenDuedate(d):
    if d.lower() == "today":
        res = datetime.now().strftime("%Y%m%d")
    elif d.lower() == "tomorrow":
        t = datetime.now() + timedelta(days = 1)
        res = t.strftime("%Y%m%d")
    else:
        res = 0
    return res


def loadTasks():
    tasks = loadFromStorage()
    tasks_sorted = sorted(tasks, key = lambda i: i["due_by"])
    print(tasks_sorted)
    tasks_rendered_date = []
    for t in tasks_sorted:
        tasks_rendered_date.append(renderDate(t))
    return tasks_rendered_date

def loadFromStorage():
    task_list = []
    dir = "peptask/tasks/active/"
    tasks_files = os.listdir(dir)
    for f in tasks_files:
        path = dir + f
        fo = open(path)
        task_data = fo.read(); fo.close()
        d = json.loads(task_data)
        task_list.append(d)
    return task_list

def renderDate(task_data):
    dt_object = datetime.strptime(task_data["due_by"], "%Y%m%d")
    task_data["due_by"] = dt_object.strftime("%A, %B %d")
    return task_data

def completeTask(id):
    id = str(id)
    act_dir = "peptask/tasks/active/"
    comp_dir = "peptask/tasks/completed/"
    task_file = act_dir + id
    move_active = "mv {} {}".format(task_file, comp_dir)
    os.system(move_active)
