import streamlit as st
import os
from streamlit.components.v1 import html
from my_app.tools.edit_image import crop_to_circle

def render_side_bar():

    # Process the image
    circle_image = crop_to_circle("data/pro_image.jpg")

    # Save or display in Streamlit
    circle_image.save("data/circle_image.png")
    st.sidebar.image("data/circle_image.png")

    # Contact Info header
    st.sidebar.header("Contact")

    # Add Email
    st.sidebar.markdown(
        """
        <a href="mailto:yousseftrabelsi250@gmail.com" target="_blank">
            <img src="https://img.icons8.com/ios-filled/50/000000/mail.png" width="20"/> yousseftrabelsi250@gmail.com
        </a>
        """, unsafe_allow_html=True
    )

    # Add Phone number (using Font Awesome icon)
    st.sidebar.markdown(
        """
        <a href="tel:+33 6 48 96 52 89" target="_blank">
            <img src="https://img.icons8.com/ios-filled/50/000000/phone.png" width="20"/> +33 6 48 96 52 89
        </a>
        """, unsafe_allow_html=True
    )

    # Add LinkedIn
    st.sidebar.markdown(
        """
        <a href="https://www.linkedin.com/in/youssef-trabelsi-b57b53263/" target="_blank">
            <img src="https://img.icons8.com/ios-filled/50/000000/linkedin.png" width="20"/> LinkedIn
        </a>
        """, unsafe_allow_html=True
    )

    # Add other social links or contact info if needed
    # For example, GitHub or Twitter:
    st.sidebar.markdown(
        """
        <a href="https://github.com/YoussefTrabelsi1" target="_blank">
            <img src="https://img.icons8.com/ios-filled/50/000000/github.png" width="20"/> GitHub
        </a>
        """, unsafe_allow_html=True
    )
    st.sidebar.markdown(
        """
        <img src="https://img.icons8.com/ios-filled/50/000000/worldwide-location.png" width="20"/> Île-de-France, France
        """, unsafe_allow_html=True
    )

    us_flag_path = os.path.join("data", "US.png")  # Update with the correct path to your US flag image
    france_flag_path = os.path.join("data", "france.png")  # Update with the correct path to your France flag image

    # Language selection dropdown with local flag images
    language = st.sidebar.selectbox(
        label="",
        options=["English", "Français"],
        index=0,  # Default to English
        
    )
    return language
