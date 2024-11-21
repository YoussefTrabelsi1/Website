import base64
import streamlit as st
import os
from streamlit.components.v1 import html
from my_app.tools.edit_image import crop_to_circle

def render_side_bar():

    """ # pages = ["Transcription", "Summaries", "Resume"]
    pages = ["Transcription", "Compte-rendu", "Affichage des Comptes Rendus"]
    page_icons = ["person-fill-slash", "file-earmark-arrow-up-fill", "database-fill", "chat-square-text-fill"]

    with st.sidebar:
        favicon_html = f'''
        <div style="display: flex; justify-content: center; align-items: center; height: 100px; margin-top: -15px ">
            <img src="data:image/x-icon;base64,{base64.b64encode(open(favicon_path, "rb").read()).decode()}" width="60" height="60">
        </div>
        '''
        st.sidebar.markdown(favicon_html, unsafe_allow_html=True)"""

    # Process the image
    circle_image = crop_to_circle("data/pro_image.jpg")

    # Save or display in Streamlit
    circle_image.save("data/circle_image.png")
    with st.sidebar:
        favicon_html = f'''
        <div style="display: flex; justify-content: center; align-items: center; height: 100px; margin-top: -15px ">
            <img src="data:image/x-icon;base64,{base64.b64encode(open("data/circle_image.png", "rb").read()).decode()}" width="150" height="150">
        </div>
        '''
        st.sidebar.markdown(favicon_html, unsafe_allow_html=True)
    #st.sidebar.image("data/circle_image.png",width=150, output_format = "PNG")

    # Contact Info header
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.markdown(
        """
        <style>
        .centered-header {
            text-align: center;
            font-size: 1.5em; /* Adjust the font size as needed */
            font-weight: bold; /* Optional: Make the text bold */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Use the custom class to center the header
    st.sidebar.markdown('<div class="centered-header">Youssef Trabelsi</div>', unsafe_allow_html=True)

    st.sidebar.markdown(
        """
        <div style="display: flex; align-items: center; margin-bottom: 10px;">
            <a href="https://www.linkedin.com/in/youssef-trabelsi-b57b53263/" target="_blank" style="margin-right: 20px;">
                <img src="https://img.icons8.com/ios-filled/50/000000/linkedin.png" width="25" />
            </a>
            <a href="https://github.com/YoussefTrabelsi1" target="_blank" style="margin-right: 20px;">
                <img src="https://img.icons8.com/ios-filled/50/000000/github.png" width="25" />
            </a>
            <a href="mailto:yousseftrabelsi250@gmail.com" target="_blank" style="margin-right: 20px;">
                <img src="https://img.icons8.com/ios-filled/50/000000/mail.png" width="25" />
            </a>
            <a href="tel:+33 6 48 96 52 89" target="_blank" style="margin-right: 20px;>
                <img src="https://img.icons8.com/ios-filled/50/000000/phone.png" width="25" />
            </a>
            <img src="https://img.icons8.com/ios-filled/50/000000/worldwide-location.png" width="20"/>
            <span>Île-de-France, France</span>
        </div>

        """, unsafe_allow_html=True
    )


    st.sidebar.header("About me")
    st.sidebar.write("""
            I am a passionate and adaptable data enthusiast, eager to embrace new tools and technologies. 
            Motivated by technical challenges, I strive to continuously learn and contribute to dynamic teams 
            by developing impactful solutions for ambitious projects.
        """)
    
    skills = ["SQL", "Python", "Snowflake", "DBT", "Spark", "Sampling techniques","AI", "Data Science", "Project management", "GitHub", "Java", "R"]

    # Sidebar
    st.sidebar.markdown("### Skills")

    # Create columns for the skills
    st.sidebar.markdown("SQL | Python | Snowflake | DBT | Spark | AI | Data Science | Project management | GitHub | Java | R")

