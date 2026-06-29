"""
task.py

Defines the Task class used throughout the Smart Task Manager application.
"""

from __future__ import annotations

import uuid
from datetime import date, datetime


class Task:
    """
    Represents a single task in the Smart Task Manager.
    """

    def __init__(
        self,
        title: str,
        description: str,
        priority: str,
        category: str,
        due_date: date,
        estimated_hours: float,
    ) -> None:

        self.task_id = str(uuid.uuid4())[:8]

        self.title = title.strip()
        self.description = description.strip()
        self.priority = priority
        self.category = category
        self.due_date = due_date
        self.estimated_hours = estimated_hours

        self.status = "Pending"

        self.created_date = datetime.now()

    def mark_completed(self) -> None:
        """
        Marks the task as completed.
        """
        self.status = "Completed"

    def is_overdue(self) -> bool:
        """
        Returns True if the task is overdue.
        """

        return (
            self.status == "Pending"
            and self.due_date < date.today()
        )

    def to_dict(self) -> dict:
        """
        Converts the Task object into a dictionary.
        """

        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "category": self.category,
            "due_date": self.due_date.isoformat(),
            "estimated_hours": self.estimated_hours,
            "status": self.status,
            "created_date": self.created_date.isoformat(),
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        """
        Creates a Task object from a dictionary.
        """

        task = cls(
            title=data["title"],
            description=data["description"],
            priority=data["priority"],
            category=data["category"],
            due_date=date.fromisoformat(data["due_date"]),
            estimated_hours=data["estimated_hours"],
        )

        task.task_id = data["task_id"]
        task.status = data["status"]
        task.created_date = datetime.fromisoformat(data["created_date"])

        return task

    def __str__(self) -> str:
        return (
            f"[{self.status}] "
            f"{self.title} "
            f"({self.priority}) "
            f"- Due: {self.due_date}"
        )
    