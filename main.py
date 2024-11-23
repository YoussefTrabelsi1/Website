import streamlit as st
from my_app.pages.main_page import render_main_page

def main():
    st.set_page_config(
    page_title="My Portfolio",
    page_icon="🌟",
    layout="centered",
    initial_sidebar_state="expanded"  # Sidebar starts open
)

    # Navigation menu for different pages
    render_main_page()

if __name__ == "__main__":
    main()
