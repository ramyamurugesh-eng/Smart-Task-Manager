"""
app.py

Main entry point for the Smart Task Manager application.
"""

import streamlit as st

from managers.task_manager import TaskManager
from services.analytics import Analytics

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Smart Task Manager",
    page_icon="📋",
    layout="wide",
)

# -------------------------------
# Load Data
# -------------------------------
manager = TaskManager()
tasks = manager.view_tasks()
analytics = Analytics(tasks)

# -------------------------------
# Title
# -------------------------------
st.title("📋 Smart Task Manager")

st.write(
    "Manage your daily tasks efficiently using Python, OOP, JSON Storage, and Streamlit."
)

st.divider()

# -------------------------------
# Dashboard Metrics
# -------------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Tasks", analytics.total_tasks())
col2.metric("Completed", analytics.completed_tasks())
col3.metric("Pending", analytics.pending_tasks())
col4.metric("Completion %", f"{analytics.completion_rate()}%")

st.divider()

# -------------------------------
# Task List
# -------------------------------
st.subheader("Current Tasks")

if not tasks:
    st.info("No tasks available.")
else:
    for task in tasks:
        st.write(task)