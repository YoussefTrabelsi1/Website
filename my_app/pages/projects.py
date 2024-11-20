import streamlit as st
from my_app.widgets.project_grid import render_projects

def projects_page():
    st.header("Projects")

    # Displaying the grid of projects using the widget
    render_projects()
