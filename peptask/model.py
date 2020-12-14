def newTask(title, due_date):
    # data validation
    if not isalnum(title):
        error = "Title must be alpha-numeric."
        return error
    from datetime import datetime as dt
    fmnow = dt.now().strftime("%Y%m%d")
    if due_date < fmnow:
        error = "Due date cannot be in the past."
        return error
    # get the latest unique id
    l = open("peptask/tasks/_latest")
    last_unique = l.read(); l.close()
    last_unique += 1
    l = open("peptask/tasks/_latest", "w")
    l.write(last_unique); l.close()
    # writing the file
    new_task_file = '{ "title": {}, "due_by": {} }'.format(title, due_date)
    nt = open("peptask/tasks/active/{}".format(last_unique), "x")
    nt.write(new_task_file); nt.close()


def loadTasks():
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
    return tasks
