import getpass
from datetime import datetime, date
from sql_comands import convert_tasks_to_df, load_df_to_sqlite
from enum import Enum
import pandas as pd


class Task:
    def __init__(self, project: str, title: str, description: str, priority: int, category: str, reference_path: str):
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
        self.task_list_table_name = self.project.lower() + '-task_list'

    def set_last_modified(self) -> None:
        self.last_modified_by = getpass.getuser()
        self.last_modified = datetime.now()

    def complete(self):
        self.completed = True
        self.load_task_to_db()

    def delete(self):
        self.logic_del = 1
        self.load_task_to_db()

    def set_due_by(self, date: datetime):
        self.due_by = date
        self.load_task_to_db()

    def update_title(self, new_title: str):
        self.title = new_title
        self.load_task_to_db()

    def is_overdue(self) -> bool:
        if self.due_by is None:
            print('No due date set')
            return False
        if self.completed is False and self.due_by < datetime.now():
            return True
        else:
            return False

    def load_task_to_db(self):
        self.set_last_modified()
        task_df = convert_tasks_to_df([self])
        load_df_to_sqlite(task_df, "projects.db", self.task_list_table_name)


class ProjectKind(Enum):
    PERSONAL = "Personal"
    PROFESSIONAL = "Professional"


class Project:

    def __init__(self, project_id: int, project_name: str, project_url: str, project_desc: str, kind: ProjectKind, start: date, projected_end: date):
        self.id = project_id
        self.name: str = project_name
        self.description: str = project_desc
        self.url: str = project_url
        self.kind: ProjectKind = kind
        self.created: date = datetime.now()
        self.start_date: date = start
        self.projected_end: date = projected_end
        self.actual_end: date = None
        self.last_modified_by: str = None
        self.last_modified: datetime = None
        self.task_list: list = []
        self.set_last_modified()
        self.proj_table_name = self.name.lower() + '-proj'
        self.task_list_table_name = self.name.lower() + '-task_list'

    def set_last_modified(self) -> None:
        self.last_modified_by = getpass.getuser()
        self.last_modified = datetime.now()

    def add_task(self, task_item: Task) -> None:
        self.task_list.append(task_item)
        self.load_tasks_to_db()
        self.set_last_modified()

    def add_tasks(self, tasks: list[Task]):
        for task in tasks:
            self.task_list.append(task)
        self.load_tasks_to_db()

    def get_tasks(self) -> list[Task]:
        return self.task_list

    def get_tasks_by_assigned(self, assigned_username) -> list[Task]:
        return [task for task in self.task_list if task.logic_del == 0 and task.assigned_to == assigned_username]

    def load_tasks_to_db(self):
        task_df = convert_tasks_to_df(self.task_list)
        load_df_to_sqlite(task_df, "projects.db", self.task_list_table_name)

    def load_proj_info_to_db(self):
        proj_df = pd.DataFrame(self.__dict__)
        load_df_to_sqlite(proj_df, "projects.db", self.task_list_table_name)


