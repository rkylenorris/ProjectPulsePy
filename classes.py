import getpass
from datetime import datetime


class Task:

    def __int__(self, project: str, title: str, description: str, priority: int, category: str, reference_path: str):
        self.logic_del = 0
        self.project = project
        self.title = title
        self.description = description
        self.priority = priority
        self.category = category
        self.reference_path = reference_path
        user = getpass.getuser()
        self.created_by = user
        self.assigned_to = user
        self.last_modified_by = user
        self.last_modified = datetime.now()
        self.completed = False
        self.due_by: datetime = None

    def set_last_modified(self) -> None:
        self.last_modified_by = getpass.getuser()
        self.last_modified = datetime.now()

    def complete(self):
        self.completed = True

    def delete(self):
        self.logic_del = 1

    def set_due_by(self, date: datetime):
        self.due_by = date

    def update_title(self, new_title: str):
        self.title = new_title

    def is_overdue(self) -> bool:
        if self.due_by is None:
            print('No due date set')
            return False
        if self.completed is False and self.due_by < datetime.now():
            return True
        else:
            return False

class TaskList:

    def __int__(self, project: str, is_personal: bool):
        self.project = project
        self.personal = is_personal
        self.last_modified_by: str = None
        self.last_modified: datetime = None
        self.tasks = []
        self.set_last_modified()

    def set_last_modified(self) -> None:
        self.last_modified_by = getpass.getuser()
        self.last_modified = datetime.now()

    def add_task(self, task_item: Task) -> None:
        self.tasks.append(task_item)
        # TODO code to handle sql insert statement for new task
        self.set_last_modified()

    def get_tasks(self) -> list[Task]:
        return self.tasks

    def get_tasks_by_assigned(self, assigned_username) -> list[Task]:
        return [task for task in self.tasks if task.logic_del == 0 and task.assigned_to == assigned_username]



