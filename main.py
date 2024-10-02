from classes import Task, convert_tasks_to_df

# project: str, title: str, description: str,
# priority: int, category: str,
# reference_path: str



tasks = [
    Task('project1', 'do stuff', 'do certain stuff', 1, 'test', 'none'),
    Task('project1', 'do things', 'do certain things', 1, 'test', 'none'),
    Task('project1', 'do wild', 'do wild stuff', 1, 'test', 'none')
]

df = convert_tasks_to_df(tasks=tasks)
print(df.head())
