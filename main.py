import streamlit as st
from my_app.pages.about import about_page
from my_app.pages.projects import projects_page
from my_app.pages.contact import contact_page

def main():
    # Set the title of the app
    st.title("My Data Science Portfolio")

    # Navigation menu for different pages
    page = st.sidebar.selectbox("Select a page", ["About Me", "Projects", "Contact"])

    if page == "About Me":
        about_page()
    elif page == "Projects":
        projects_page()
    elif page == "Contact":
        contact_page()

if __name__ == "__main__":
    main()
