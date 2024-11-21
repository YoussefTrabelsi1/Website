import streamlit as st
import base64

def display_projects(projects):
    # CSS styling
    css = """
    <style>
        .container {
            display: flex;
            justify-content: space-between;
            width: 1000px;
            margin-left: -150px;
        }
        .col1, .col2 {
            width: 600px;
            flex-direction: column;
            align-items: center;
            text-align: center;
        }
        img {
            margin-bottom: 20px;
        }
    </style>
    """
    
    # Initialize HTML content for the projects
    image_html = f"{css}<div class='container'>"
    
    # Loop through projects and add them to the HTML content
    for i, project in enumerate(projects):
        image_html += f"""
            <div class="col{i%2 + 1}">
                <h3>{project['name']}</h3>
                <img src="data:image/x-icon;base64,{base64.b64encode(open(project['image_path'], 'rb').read()).decode()}" width="400" height="300">
                <p>{project['description']}</p>
                <p><strong>Skills</strong>: {project['skills']}</p>
                <p><strong>Languages</strong>: {project['languages']}</p>
                <p><a href="{project['github_repo']}">GitHub Repository</a></p>
            </div>
        """
    
    # Close the container div and render the HTML
    image_html += "</div>"
    st.markdown(image_html, unsafe_allow_html=True)

def render_projects():
    
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
                align-items: center;  /* Centers content horizontally within each column */
                text-align: center;
            }
        </style>"""
    image_html=f"""
        {css}
        <div class="container">
            <div class="col1">
                <h3>Detecting Periapical Lesions on Dental X-rays</h3>
                <img src="data:image/x-icon;base64,{base64.b64encode(open("data/projects/Lesions.jpg", "rb").read()).decode()}" width="400" height="300">
                <p>Developed an AI algorithm to detect peri-apical lesions in dental panoramic radiographs using convolutional neural networks (CNN) and YOLOv8 architecture. Achieved a remarkable 99% accuracy after extensive training and model optimization.</p>
                <p><strong>Skills</strong>: Deep learning, CNNs, YOLOv8, Computer vision, AI, Data Science, Project management, GitHub</p>
                <p><strong>Languages</strong>: Python, TensorFlow, yolov8, Bash</p>
                <p><a href="https://github.com/YoussefTrabelsi1/Peri-apical-lesions-detection/tree/main">GitHub Repository</a></p>
            </div>
            <div class="col2">
                <h3>Drug and disease search engine</h3>
                <img src="data:image/x-icon;base64,{base64.b64encode(open("data/projects/gmd_research_result.png", "rb").read()).decode()}" width="400" height="300">
                <p>Developed a medical search engine with a JavaFX interface for identifying diseases and medications linked to symptoms. Used Hadoop and Apache for large-scale data management.</p>
                <p><strong>Skills</strong>: Big data, Hadoop, Apache Spark, JavaFX, Python, Data mapping, GitHub, Algorithms, Database design</p>
                <p><strong>Languages</strong>: Java, Python, Hadoop</p>
                <p><a href="https://github.com/your_project_link">GitHub Repository</a></p>
            </div>
        </div>
    """

    st.markdown(image_html, unsafe_allow_html=True)

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

