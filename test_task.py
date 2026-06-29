from managers.task_manager import TaskManager
from services.analytics import Analytics

# Load all tasks
manager = TaskManager()

# Create analytics object
analytics = Analytics(manager.view_tasks())

print("\n===== TASK ANALYTICS =====\n")

print(f"Total Tasks      : {analytics.total_tasks()}")
print(f"Completed Tasks  : {analytics.completed_tasks()}")
print(f"Pending Tasks    : {analytics.pending_tasks()}")
print(f"Overdue Tasks    : {analytics.overdue_tasks()}")
print(f"Completion Rate  : {analytics.completion_rate()}%")