"""
analytics.py

Provides analytics and statistics for tasks.
"""

from models.task import Task


class Analytics:
    """
    Performs analytics on a list of tasks.
    """

    def __init__(self, tasks: list[Task]):
        self.tasks = tasks

    def total_tasks(self) -> int:
        return len(self.tasks)

    def completed_tasks(self) -> int:
        return sum(task.status == "Completed" for task in self.tasks)

    def pending_tasks(self) -> int:
        return sum(task.status == "Pending" for task in self.tasks)

    def overdue_tasks(self) -> int:
        return sum(task.is_overdue() for task in self.tasks)

    def completion_rate(self) -> float:
        if not self.tasks:
            return 0.0

        return round(
            self.completed_tasks() / self.total_tasks() * 100,
            2
        )