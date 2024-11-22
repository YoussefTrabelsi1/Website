import streamlit as st
from my_app.widgets.project_grid import render_projects
from my_app.widgets.sidebar import render_side_bar
from my_app.widgets.experiences import render_exp
from my_app.widgets.education import render_education
from my_app.widgets.contact import render_contact

def render_main_page():
    
    render_side_bar()
    render_projects()
    render_exp()
    render_education()
    render_contact()