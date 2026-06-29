"""
Add Task Page
"""

import streamlit as st
from datetime import date

from managers.task_manager import TaskManager
from models.task import Task

st.title("➕ Add New Task")

manager = TaskManager()

with st.form("add_task_form"):

    title = st.text_input("Task Title")

    description = st.text_area("Description")

    priority = st.selectbox(
        "Priority",
        ["High", "Medium", "Low"]
    )

    category = st.selectbox(
        "Category",
        [
            "Work",
            "Study",
            "Personal",
            "Project",
            "Health",
            "Other",
        ],
    )

    due_date = st.date_input(
        "Due Date",
        value=date.today()
    )

    estimated_hours = st.number_input(
        "Estimated Hours",
        min_value=1,
        max_value=100,
        value=1
    )

    submitted = st.form_submit_button("Add Task")

    if submitted:

        task = Task(
            title=title,
            description=description,
            priority=priority,
            category=category,
            due_date=due_date,
            estimated_hours=estimated_hours,
        )

        manager.add_task(task)

        st.success("✅ Task added successfully!")