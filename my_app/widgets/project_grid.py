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
            <h3>{projects[0]['name']}</h3>
            <img src="data:image/x-icon;base64,{base64.b64encode(open(projects[0]['image_path'], 'rb').read()).decode()}" width="400" height="300">
            <p>{projects[0]['description']}</p>
            <p><strong>Skills</strong>: {projects[0]['skills']}</p>
            <p><strong>Languages</strong>: {projects[0]['languages']}</p>
            <p><a href="{projects[0]['github_repo']}">GitHub Repository</a></p>
        </div>
        <div class="col2">
            <h3>{projects[1]['name']}</h3>
            <img src="data:image/x-icon;base64,{base64.b64encode(open(projects[1]['image_path'], 'rb').read()).decode()}" width="400" height="300">
            <p>{projects[1]['description']}</p>
            <p><strong>Skills</strong>: {projects[1]['skills']}</p>
            <p><strong>Languages</strong>: {projects[1]['languages']}</p>
            <p><a href="{projects[1]['github_repo']}">GitHub Repository</a></p>
        </div>
    """
    
    # Close the container div and render the HTML
    image_html += "</div>"
    st.markdown(image_html, unsafe_allow_html=True)

def render_projects():

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
        'name': 'Compiler',
        'image_path': 'data/projects/compiler.webp',  # Replace with actual image path
        'description': 'Developed a Java-based compiler respecting formal language theory. Defined syntax and semantics for translating source to target languages, deepening knowledge of automata theory and syntax analysis.',
        'skills': 'Compiler design, Java, Formal languages, Automata theory, Syntax analysis, Project management',
        'languages': 'Java',
        'github_repo': 'https://github.com/your_project_link'
    }]
    display_projects(projects2)
    # Project 4: Flash Cards
    st.subheader("Flash Cards")
    st.write("Created a flashcard application using JavaFX with MVC architecture. Included sophisticated algorithms to manage card appearance and integrated user statistics for learning efficiency.")
    st.write("**Skills**: Data analysis, Database design, Object-oriented programming, MVC architecture, JavaFX, Statistics, Project management")
    st.write("**Languages**: Java")
    st.write("[GitHub Repository](https://github.com/your_project_link)")

    # Project 5: Projet Compilateur
    st.subheader("Compiler")
    st.write("Developed a Java-based compiler respecting formal language theory. Defined syntax and semantics for translating source to target languages, deepening knowledge of automata theory and syntax analysis.")
    st.write("**Skills**: Compiler design, Java, Formal languages, Automata theory, Syntax analysis, Project management")
    st.write("**Languages**: Java")
    st.write("[GitHub Repository](https://github.com/your_project_link)")

    # Project 2: Moteur de Recherche de Maladies et Médicaments
    st.subheader("Facies Classification by Machine Learning")
    st.write("Built a machine learning model to classify geological facies using data from wells. Applied Random Forest and PCA using Scikit-learn, achieving 61.4% accuracy on complex geological data.")
    st.write("**Skills**: Data modeling, Random Forest, PCA, Data science, Project management, GitHub, Supervised learning")
    st.write("**Languages**: Python, Scikit-learn")
    st.write("[GitHub Repository](https://github.com/your_project_link)")

    # Project 6: Wordeul
    st.subheader("Wordeul")
    st.write("Created a custom version of the Wordle game using Python and Flask, including a solver written in C that optimizes the word search algorithm. Integrated information theory to enhance solver efficiency.")
    st.write("**Skills**: Algorithm optimization, Information theory, Flask, C programming, Game development, Project management")
    st.write("**Languages**: Python, C, Flask")
    st.write("[GitHub Repository](https://github.com/your_project_link)")

    # Project 7: Civic'TN
    st.subheader("Civic'TN")
    st.write("Developed a civic engagement application to improve interactions between citizens and public institutions. Used PostgreSQL for database management, Python with Flask for server-side logic, and HTML/CSS for the user interface.")
    st.write("**Skills**: Civic technology, Web development, PostgreSQL, Python, Flask, HTML/CSS, Project management")
    st.write("**Languages**: Python, Flask, PostgreSQL, HTML, CSS")
    st.write("[GitHub Repository](https://github.com/your_project_link)")


if 0:
    grid1,grid2=st.columns(2)
    with grid1:
        # Project 1: Détection des Lésions Péri-apicales sur Radiographies Dentaires
        st.subheader("Detecting Periapical Lesions on Dental X-rays")
        st.image("data/projects/Lesions.jpg")
        st.write("Developed an AI algorithm to detect peri-apical lesions in dental panoramic radiographs using convolutional neural networks (CNN) and YOLOv8 architecture. Achieved a remarkable 99% accuracy after extensive training and model optimization.")
        st.write("**Skills**: Deep learning, CNNs, YOLOv8, Computer vision, AI, Data Science, Project management, GitHub")
        st.write("**Languages**: Python, TensorFlow, yolov8, Bash")
        st.write("[GitHub Repository](https://github.com/YoussefTrabelsi1/Peri-apical-lesions-detection/tree/main)")

    with grid2:
        # Project 3: Moteur de Recherche Médical
        st.subheader("Drug and disease search engine")
        """col1,col2=st.columns(2)
        with col1:
            st.image("data\projects\gmd_main.png")
        with col2:"""
        st.image("data\projects\gmd_research_result.png")
        st.write("Developed a medical search engine with a JavaFX interface for identifying diseases and medications linked to symptoms. Used Hadoop and Apache for large-scale data management.")
        st.write("**Skills**: Big data, Hadoop, Apache Spark, JavaFX, Python, Data mapping, GitHub, Algorithms, Database design")
        st.write("**Languages**: Java, Python, Hadoop")
        st.write("[GitHub Repository](https://github.com/your_project_link)")

