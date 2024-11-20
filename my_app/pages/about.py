import streamlit as st
from my_app.widgets.project_grid import render_projects

def about_page():
    st.header("À propos de moi")
    
    # About text
    st.write("""
        Hello, I'm a Data Scientist and Engineer. I specialize in building data pipelines, data analysis, 
        and machine learning models. I enjoy working with data to derive actionable insights and solve problems.
    """)
    
    # Display photo
    st.image("data\pro_image.jpg", caption="Your Photo", width=150)
    
    # CV Preview (just an example; link to a PDF or create your own preview)
    st.download_button("Download CV", "path_to_cv.pdf")

    # Render project grid (a placeholder for now)
    render_projects()

