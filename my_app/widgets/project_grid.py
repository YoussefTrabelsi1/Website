import streamlit as st
from my_app.tools.display_projects import display_projects_streamlit

def render_projects():
    st.markdown('<h1 style="color: #3395c4;">Projects :</h1>', unsafe_allow_html=True)

    # Consolidated list of projects
    projects = [
        {
            'name': 'Detecting Periapical Lesions on Dental X-rays',
            'image_path': 'data/projects/Lesions.jpg',
            'description': 'Developed an AI algorithm to detect peri-apical lesions in dental panoramic radiographs using convolutional neural networks (CNN) and YOLOv8 architecture. Achieved a remarkable 99% accuracy after extensive training and model optimization.',
            'skills': 'Deep learning, CNNs, YOLOv8, Computer vision, AI, Data Science, Project management, GitHub',
            'languages': 'Python, TensorFlow, yolov8, Bash',
        },
        {
            'name': 'Drug side effects and disease search engine',
            'image_path': 'data/projects/gmd_research_result.png',
            'description': 'Developed a medical search engine with a JavaFX interface for identifying diseases and medications linked to symptoms. Used Hadoop and Apache for large-scale data management.',
            'skills': 'Big data, Hadoop, Apache Spark, JavaFX, Python, Data mapping, GitHub, Algorithms, Database design',
            'languages': 'Java, Python, Hadoop',
        },
        
        {
            'name': 'Facies Classification by Machine Learning',
            'image_path': 'data/projects/Facies.webp',
            'description': 'Built a machine learning model to classify geological facies using data from wells. Applied Random Forest and PCA using Scikit-learn, achieving 61.4% accuracy on complex geological data.',
            'skills': 'Data modeling, Random Forest, PCA, Data science, Project management, GitHub, Supervised learning',
            'languages': 'Python, Scikit-learn',
        }
    ]

    

    # Display all projects
    display_projects_streamlit(projects)
