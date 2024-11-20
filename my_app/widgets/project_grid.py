import streamlit as st

def render_projects():
    st.subheader("Projects")
    
    # List of project names (you could import this from a separate module)
    projects = ["Project 1", "Project 2", "Project 3"]

    # Create a grid of project blocks
    for project in projects:
        col = st.columns(3)[0]  # Define the number of columns in the grid
        with col:
            # Display project name as a clickable button (for now it will print in the terminal)
            if st.button(f"Button to {project}"):
                print(f"Button for {project} clicked!")
