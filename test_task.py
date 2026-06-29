from datetime import date
from models.task import Task

# Create a sample task
task = Task(
    title="Complete Smart Task Manager",
    description="Build the backend using Python OOP",
    priority="High",
    category="Project",
    due_date=date(2026, 7, 5),
    estimated_hours=4,
)

# Display the task
print(task)

# Display the task as a dictionary
print(task.to_dict())