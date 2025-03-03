from my_app.widgets.project_grid import render_projects
from my_app.widgets.experiences import render_exp
from my_app.widgets.education import render_education
from my_app.widgets.contact import render_contact
from my_app.widgets.sidebar import render_side_bar
import streamlit as st

def render_main_page():
    # Navigation Tabs
    tabs = st.tabs(["Experiences", "Projects", "Education", "Contact"])
    render_side_bar()

    # Dynamic rendering of content
    with tabs[0]:
        render_exp()
    with tabs[1]:
        render_projects()
    with tabs[2]:
        render_education()
    with tabs[3]:
        render_contact()

if __name__ == "__main__":
    render_side_bar()
    render_main_page()
