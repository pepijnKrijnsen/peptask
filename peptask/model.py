def newTask():
    pass

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
