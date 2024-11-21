import streamlit as st
from my_app.widgets.project_grid import render_projects
from my_app.widgets.sidebar import render_side_bar
from my_app.widgets.about import about_section


def render_main_page():
    

    langage=render_side_bar()
    

    st.subheader("Projects : ")

    # Displaying the grid of projects using the widget
    render_projects()

    st.header("Contact Me")
    
    # Displaying contact information
    st.subheader("You can reach me at:")
    
    # Displaying email and LinkedIn contact
    st.write("Email: example@mail.com")
    st.write("LinkedIn: [Your LinkedIn Profile](https://www.linkedin.com/in/yourprofile)")
    
    # Optionally, include a contact form for people to reach you directly
    with st.form(key='contact_form'):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        
        # Submit button
        submit_button = st.form_submit_button(label='Send Message')
        if submit_button:
            st.write(f"Thank you {name}! I'll get back to you shortly.")