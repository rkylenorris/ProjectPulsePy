from enum import Enum
from pathlib import Path

def enum_from_config():
    kinds = ["PERSONAL", "PROFESSIONAL"]
    with open("pulse_config/kind.txt", 'r') as f:
        lines = f.readlines()
        if len(lines) > 0:
            for line in lines:
                kinds.append(line.upper().strip(" \n"))

    return Enum("ProjectKind", {s: i for i, s in enumerate(kinds)})


ProjectKind = enum_from_config()


class PulseConfig:

    def __init__(self, project_path: str, project_name: str, project_kind: ProjectKind):
        self.path = project_path
        self.project_name = project_name
        self.kind = project_kind
        if self.kind.value != 0:
            self.db_path = Path(project_path) / f"pulse/{project_name}.db"
        else:
            self.db_path = Path.home() / f"pulse/{project_name}.db"

