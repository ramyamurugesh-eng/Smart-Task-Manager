"""
storage.py

Handles saving and loading tasks from a JSON file.
"""

from __future__ import annotations

import json
from pathlib import Path

from models.task import Task


class Storage:
    """
    Handles persistence of Task objects using a JSON file.
    """

    def __init__(self, file_path: str = "data/tasks.json") -> None:
        self.file_path = Path(file_path)

        # Create the data folder if it doesn't exist
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

    def save_tasks(self, tasks: list[Task]) -> None:
        """
        Save all tasks to the JSON file.
        """

        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(
                [task.to_dict() for task in tasks],
                file,
                indent=4,
            )

    def load_tasks(self) -> list[Task]:
        """
        Load tasks from the JSON file.
        """

        if not self.file_path.exists():
            return []

        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

            return [Task.from_dict(item) for item in data]

        except (json.JSONDecodeError, FileNotFoundError):
            return []