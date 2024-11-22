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
        num_projects = len(projects)
        for i in range(0, num_projects - 1, 2):  # Display projects in pairs
            cols = st.columns(2)
            for col, project in zip(cols, projects[i:i+2]):
                with col:
                    st.container()
                    st.subheader(project['name'])
                    st.image(project['image_path'])
                    st.write(project['description'])
                    st.write("**Skills learned:**")
                    st.write(project['skills'])
                    st.write("**Languages learned:**")
                    st.write(project['languages'])

        # Check if odd number of projects and display the last one
        if num_projects % 2 != 0:
            last_project = projects[-1]
            st.container()
            st.subheader(last_project['name'])
            col1,col2,col3=st.columns(3)
            with col2:
                st.image(last_project['image_path'])
            st.write(last_project['description'])
            st.write("**Skills learned:**")
            st.write(last_project['skills'])
            st.write("**Languages learned:**")
            st.write(last_project['languages'])