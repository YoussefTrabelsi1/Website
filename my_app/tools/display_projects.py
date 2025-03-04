import streamlit as st
import base64

def display_projects(projects):
    # CSS styling
    css="""<style>
        .container {
            display: flex;
            justify-content: space-between;
            width: 1000px;
            margin-left: -150px;
            gap: 50px;
        }
        .col1, .col2 {
            width: 600px;
            flex-direction: column;
            text-align: left;  /* Keep text left-aligned in the columns */

        }
        .col1 img, .col2 img {
            display: block;
            margin-left: auto;
            margin-right: auto;
            margin-bottom: 30px;  /* Adds space between the image and the description */
        }
    </style>"""
    
    # Initialize HTML content for the projects
    image_html = f"""
    {css}
    <div class='container'>"""
    # Loop through projects and add them to the HTML content
    image_html += f"""
        <div class="col1">
            <h4>{projects[0]['name']}</h4>
            <img src="data:image/x-icon;base64,{base64.b64encode(open(projects[0]['image_path'], 'rb').read()).decode()}" width="400" height="300">
            <p>{projects[0]['description']}</p>
            <p><strong>Skills</strong>: {projects[0]['skills']}</p>
            <p><strong>Languages</strong>: {projects[0]['languages']}</p>
        </div>
        <div class="col2">
            <h4>{projects[1]['name']}</h4>
            <img src="data:image/x-icon;base64,{base64.b64encode(open(projects[1]['image_path'], 'rb').read()).decode()}" width="400" height="300">
            <p>{projects[1]['description']}</p>
            <p><strong>Skills</strong>: {projects[1]['skills']}</p>
            <p><strong>Languages</strong>: {projects[1]['languages']}</p>
        </div>
    """
    
    # Close the container div and render the HTML
    image_html += "</div>"
    st.markdown(image_html, unsafe_allow_html=True)

# Function to display projects
def display_projects_streamlit(projects):
    for project in projects:
        st.container()
        st.subheader(project['name'])
        if "facies" in project['image_path'].lower():
            col1,col2=st.columns(2)
            with col1:
                st.image("data/projects/Facies.webp")
            with col2:
                st.image("data/projects/Facies.png",width=270)
        else:
            try:
                st.image(project['image_path'])
            except FileNotFoundError:
                print("Image not found")
        
        st.write(f"**Problem Statement:** {project['problem_statement']}")
        st.write("**My Role:**")
        #st.markdown("<ul>", unsafe_allow_html=True)
        for role_point in project['role'].split(';'):
            st.markdown(f"<li>{role_point.strip()}</li>", unsafe_allow_html=True)
        st.markdown("</ul>", unsafe_allow_html=True)
        st.write(f"**Tools/Technologies Used:** {project['tools']}")
        st.write("**Description:**")
        st.write(project['description'])
        st.markdown("---")  # Add a horizontal divider between projects

