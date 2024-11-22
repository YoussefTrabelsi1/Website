import streamlit as st
from my_app.tools.display_projects import display_projects_streamlit

def render_projects():
    st.markdown('<h1 style="color: #3395c4;">Projects :</h1>', unsafe_allow_html=True)

    # Consolidated list of projects
    projects = [
        {
            'name': 'Detecting Periapical Lesions on Dental X-rays',
            'image_path': 'data/projects/Lesions.jpg',
            'problem_statement': 'Dental panoramic radiographs often fail to clearly reveal peri-apical lesions, leading to diagnostic errors. An AI-driven solution was needed to improve diagnostic accuracy.',
            'role': 'Designed and trained CNN models; Optimized YOLOv8 for object detection; Conducted extensive data preprocessing and testing; Managed project workflow and results analysis.',
            'tools': 'Python, TensorFlow, YOLOv8, Bash, GitHub',
            'description': 'Developed an AI algorithm to detect peri-apical lesions in dental panoramic radiographs using CNNs and YOLOv8 architecture. Achieved a remarkable 99% accuracy.',
        },
        {
            'name': 'Drug Side Effects and Disease Search Engine',
            'image_path': 'data/projects/gmd_research_result.png',
            'problem_statement': 'Patients often struggle to find comprehensive information linking symptoms to diseases or medications. A scalable, interactive solution was required to manage vast amounts of medical data.',
            'role': 'Designed a scalable database architecture; Implemented Hadoop and Spark for data processing; Developed a user interface using JavaFX; Integrated Python scripts for data mapping and results generation.',
            'tools': 'Java, Python, Hadoop, Apache Spark, JavaFX, GitHub',
            'description': 'Developed a medical search engine with a JavaFX interface for identifying diseases and medications linked to symptoms. Used Hadoop and Apache for large-scale data management.',
        },
        {
            'name': 'Facies Classification by Machine Learning',
            'image_path': 'data/projects/Facies.webp',
            'problem_statement': 'Geologists faced challenges in classifying geological facies accurately due to complex datasets from oil wells. A machine learning model was needed for better predictive accuracy.',
            'role': 'Engineered data preprocessing pipelines; Developed classification models using Random Forest; Applied PCA for dimensionality reduction; Evaluated and refined models for better accuracy.',
            'tools': 'Python, Scikit-learn, GitHub',
            'description': 'Built a machine learning model to classify geological facies using data from wells. Applied Random Forest and PCA, achieving 61.4% accuracy on complex geological data.',
        }
    ]


    

    # Display all projects
    display_projects_streamlit(projects)
