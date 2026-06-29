"""
task_manager.py

Contains the business logic for managing tasks.
"""

from models.task import Task
from services.storage import Storage


class TaskManager:
    """
    Handles all task-related operations.
    """

    def __init__(self):
        """
        Initialize TaskManager by loading existing tasks.
        """
        self.storage = Storage()
        self.tasks = self.storage.load_tasks()

    def add_task(self, task: Task) -> None:
        """
        Add a new task.
        """
        self.tasks.append(task)
        self.storage.save_tasks(self.tasks)

    def view_tasks(self) -> list[Task]:
        """
        Return all tasks.
        """
        return self.tasks

    def delete_task(self, task_id: str) -> bool:
        """
        Delete a task by its ID.
        """
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                self.storage.save_tasks(self.tasks)
                return True

        return False

    def mark_task_completed(self, task_id: str) -> bool:
        """
        Mark a task as completed.
        """
        for task in self.tasks:
            if task.task_id == task_id:
                task.mark_completed()
                self.storage.save_tasks(self.tasks)
                return True

        return False

    def update_task(
        self,
        task_id: str,
        title: str,
        description: str,
        priority: str,
        category: str,
        due_date,
        estimated_hours: int,
    ) -> bool:
        """
        Update an existing task.
        """
        for task in self.tasks:
            if task.task_id == task_id:
                task.title = title
                task.description = description
                task.priority = priority
                task.category = category
                task.due_date = due_date
                task.estimated_hours = estimated_hours

                self.storage.save_tasks(self.tasks)
                return True

        return False