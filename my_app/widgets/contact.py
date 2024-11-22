import streamlit as st

def render_contact():
    st.markdown('<h1 style="color: #3395c4;">Contact Me</h1>', unsafe_allow_html=True)
    
    # Displaying contact information
    st.subheader("You can reach me at:")
    
    # Displaying email and LinkedIn contact
    st.write("Email: yousseftrabelsi250@gmail.com")
    st.write("LinkedIn: [Youssef Trabelsi](https://www.linkedin.com/in/youssef-trabelsi-b57b53263/)")
    