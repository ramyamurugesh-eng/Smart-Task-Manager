from datetime import date

from models.task import Task
from services.storage import Storage

# Create storage object
storage = Storage()

# Create sample tasks
task1 = Task(
    title="Complete Smart Task Manager",
    description="Build backend using Python OOP",
    priority="High",
    category="Project",
    due_date=date(2026, 7, 5),
    estimated_hours=4,
)

task2 = Task(
    title="Prepare README",
    description="Write project documentation",
    priority="Medium",
    category="Documentation",
    due_date=date(2026, 7, 10),
    estimated_hours=2,
)

# Save tasks
storage.save_tasks([task1, task2])

print("Tasks saved successfully!")

# Load tasks
loaded_tasks = storage.load_tasks()

print("\nLoaded Tasks:\n")

for task in loaded_tasks:
    print(task)