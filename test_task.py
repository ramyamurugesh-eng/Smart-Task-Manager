from datetime import date

from managers.task_manager import TaskManager
from models.task import Task

# Create TaskManager
manager = TaskManager()

# Create a new task
task = Task(
    title="Learn Streamlit",
    description="Complete the Streamlit deployment",
    priority="High",
    category="Project",
    due_date=date(2026, 7, 15),
    estimated_hours=3,
)

# Add task
manager.add_task(task)

print("Current Tasks:\n")

# Display all tasks
for task in manager.view_tasks():
    print(task)

# Mark first task as completed
first_task = manager.view_tasks()[0]
manager.mark_task_completed(first_task.task_id)

print("\nAfter Completing First Task:\n")

for task in manager.view_tasks():
    print(task)