"""
View Tasks Page
"""

import streamlit as st

from managers.task_manager import TaskManager

st.title("📋 View Tasks")

manager = TaskManager()
tasks = manager.view_tasks()

if not tasks:
    st.info("No tasks available.")
else:

    for task in tasks:

        with st.container(border=True):

            st.subheader(task.title)

            st.write(f"**Description:** {task.description}")
            st.write(f"**Priority:** {task.priority}")
            st.write(f"**Category:** {task.category}")
            st.write(f"**Status:** {task.status}")
            st.write(f"**Due Date:** {task.due_date}")
            st.write(f"**Estimated Hours:** {task.estimated_hours}")

            col1, col2 = st.columns(2)

            with col1:
                if task.status == "Pending":
                    if st.button(
                        "✅ Mark Completed",
                        key=f"complete_{task.task_id}"
                    ):
                        manager.mark_task_completed(task.task_id)
                        st.rerun()

            with col2:
                if st.button(
                    "🗑 Delete",
                    key=f"delete_{task.task_id}"
                ):
                    manager.delete_task(task.task_id)
                    st.rerun()