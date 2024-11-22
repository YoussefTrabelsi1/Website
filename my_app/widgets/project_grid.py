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

def render_projects():

    st.markdown(f'<h1 style="color: #3395c4;">Projects :</h1>', unsafe_allow_html=True)

    projects1 = [
        {
            'name': 'Detecting Periapical Lesions on Dental X-rays',
            'image_path': 'data/projects/Lesions.jpg',
            'description': 'Developed an AI algorithm to detect peri-apical lesions in dental panoramic radiographs using convolutional neural networks (CNN) and YOLOv8 architecture. Achieved a remarkable 99% accuracy after extensive training and model optimization.',
            'skills': 'Deep learning, CNNs, YOLOv8, Computer vision, AI, Data Science, Project management, GitHub',
            'languages': 'Python, TensorFlow, yolov8, Bash',
            'github_repo': 'https://github.com/YoussefTrabelsi1/Peri-apical-lesions-detection/tree/main'
        },
        {
            'name': 'Drug side effects and disease search engine ',
            'image_path': 'data/projects/gmd_research_result.png',
            'description': 'Developed a medical search engine with a JavaFX interface for identifying diseases and medications linked to symptoms. Used Hadoop and Apache for large-scale data management.',
            'skills': 'Big data, Hadoop, Apache Spark, JavaFX, Python, Data mapping, GitHub, Algorithms, Database design',
            'languages': 'Java, Python, Hadoop',
            'github_repo': 'https://github.com/your_project_link'
        }
    ]

    # Display projects
    display_projects(projects1)

    projects2=[{
        'name': 'Flash Cards',
        'image_path': 'data/projects/flashcards.webp',  # Replace with actual image path
        'description': 'Created a flashcard application using JavaFX with MVC architecture. Included sophisticated algorithms to manage card appearance and integrated user statistics for learning efficiency.',
        'skills': 'Data analysis, Database design, Object-oriented programming, MVC architecture, JavaFX, Statistics, Project management',
        'languages': 'Java',
        'github_repo': 'https://github.com/your_project_link'
    },
    {
        'name': 'Facies Classification by Machine Learning',
        'image_path': 'data/projects/Facies.webp',  # Replace with actual image path
        'description': 'Built a machine learning model to classify geological facies using data from wells. Applied Random Forest and PCA using Scikit-learn, achieving 61.4% accuracy on complex geological data.',
        'skills': 'Data modeling, Random Forest, PCA, Data science, Project management, GitHub, Supervised learning',
        'languages': 'Python, Scikit-learn',
        'github_repo': 'https://github.com/your_project_link'
    }]
    display_projects(projects2)
