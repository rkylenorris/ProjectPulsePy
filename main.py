from tasks_structure import Task, convert_tasks_to_df
from initial_setup import enum_from_config, Enum

ProjectKind: Enum = enum_from_config()
for kind in ProjectKind:
    print(kind.name)
    print(kind.value)
    print("----")

# project: str, title: str, description: str,
# priority: int, category: str,
# reference_path: str



# tasks = [
#     Task('project1', 'do stuff', 'do certain stuff', 1, 'test', 'none'),
#     Task('project1', 'do things', 'do certain things', 1, 'test', 'none'),
#     Task('project1', 'do wild', 'do wild stuff', 1, 'test', 'none')
# ]
#
# df = convert_tasks_to_df(tasks=tasks)
# print(df.head())
