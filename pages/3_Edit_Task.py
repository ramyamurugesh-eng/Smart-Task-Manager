"""
Edit Task Page
"""

import streamlit as st

from managers.task_manager import TaskManager

st.title("✏️ Edit Task")

# Create Task Manager object
manager = TaskManager()

# Load all tasks
tasks = manager.view_tasks()

# Check if tasks exist
if not tasks:
    st.info("No tasks available.")
    st.stop()

# Dictionary to map task title to task object
task_options = {task.title: task for task in tasks}

# Select a task
selected_title = st.selectbox(
    "Select Task",
    list(task_options.keys())
)

selected_task = task_options[selected_title]

# -----------------------------
# Edit Form
# -----------------------------
with st.form("edit_task_form"):

    title = st.text_input(
        "Task Title",
        value=selected_task.title
    )

    description = st.text_area(
        "Description",
        value=selected_task.description
    )

    priority = st.selectbox(
        "Priority",
        ["High", "Medium", "Low"],
        index=["High", "Medium", "Low"].index(selected_task.priority)
    )

    categories = [
        "Work",
        "Study",
        "Personal",
        "Project",
        "Health",
        "Other"
    ]

    category = st.selectbox(
        "Category",
        categories,
        index=categories.index(selected_task.category)
        if selected_task.category in categories
        else categories.index("Other")
    )

    due_date = st.date_input(
        "Due Date",
        value=selected_task.due_date
    )

    estimated_hours = st.number_input(
        "Estimated Hours",
        min_value=1,
        max_value=100,
        value=int(selected_task.estimated_hours)
    )

    submitted = st.form_submit_button("💾 Update Task")

    if submitted:

        updated = manager.update_task(
            task_id=selected_task.task_id,
            title=title,
            description=description,
            priority=priority,
            category=category,
            due_date=due_date,
            estimated_hours=estimated_hours
        )

        if updated:
            st.success("✅ Task updated successfully!")

            st.write("### Updated Task")

            st.write(f"**Title:** {title}")
            st.write(f"**Description:** {description}")
            st.write(f"**Priority:** {priority}")
            st.write(f"**Category:** {category}")
            st.write(f"**Due Date:** {due_date}")
            st.write(f"**Estimated Hours:** {estimated_hours}")

        else:
            st.error("❌ Task could not be updated.")