class Project:
    tasks = []

    def __init__(self, project_name, project_desc):
        self.name = project_name
        self.desc = project_desc

    def add_task(self, title, desc, status):
        self.tasks.append({"title": title, "desc": desc, "status": status})

    def remove_task(self, title):
        for i in self.tasks:
            if i["title"] == title:
                self.tasks.remove(i)

    def get_task_status(self, title):
        for i in self.tasks:
            if i["title"] == title:
                return i["status"]

    def update_task_status(self, title, new_status):
        for i in self.tasks:
            if i["title"] == title:
                i["status"] = new_status

    def get_tasks_by_status(self, status):
        lis = []
        for i in self.tasks:
            if i["status"] == status:
                lis.append(f"{i["title"]}")
        return lis

    def print_tasks(self):
        for i in self.tasks:
            print(f"Task: {i["title"]}, Status: {i["status"]}")

project = Project("Project name", "This is a project")
project.add_task("Task1", "Desc1", "In progress")
project.add_task("Task2", "Desc2", "Planned")
project.update_task_status("Task1", "Completed")
project.print_tasks()

planned_tasks = project.get_tasks_by_status("Planned")
print(planned_tasks)