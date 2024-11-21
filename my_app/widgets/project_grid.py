import streamlit as st

def render_projects(language):

    if language=="English":

        # Project 1: Détection des Lésions Péri-apicales sur Radiographies Dentaires
        st.subheader("Detecting Periapical Lesions on Dental X-rays")
        st.image("data/projects/Lesions.jpg")
        st.write("Developed an AI algorithm to detect peri-apical lesions in dental panoramic radiographs using convolutional neural networks (CNN) and YOLOv8 architecture. Achieved a remarkable 99% accuracy after extensive training and model optimization.")
        st.write("**Skills**: Deep learning, CNNs, YOLOv8, Computer vision, AI, Data Science, Project management, GitHub")
        st.write("**Languages**: Python, TensorFlow, yolov8, Bash")
        st.write("[GitHub Repository](https://github.com/YoussefTrabelsi1/Peri-apical-lesions-detection/tree/main)")
        

        # Project 2: Moteur de Recherche de Maladies et Médicaments
        st.subheader("Moteur de Recherche de Maladies et Médicaments")
        st.write("Built a machine learning model to classify geological facies using data from wells. Applied Random Forest and PCA using Scikit-learn, achieving 61.4% accuracy on complex geological data.")
        st.write("**Skills**: Data modeling, Random Forest, PCA, Data science, Project management, GitHub, Supervised learning")
        st.write("**Languages**: Python, Scikit-learn")
        st.write("[GitHub Repository](https://github.com/your_project_link)")

        # Project 3: Moteur de Recherche Médical
        st.subheader("Moteur de Recherche Médical")
        st.write("Developed a medical search engine with a JavaFX interface for identifying diseases and medications linked to symptoms. Used Hadoop and Apache for large-scale data management.")
        st.write("**Skills**: Big data, Hadoop, Apache Spark, JavaFX, Python, Data mapping, GitHub, Algorithms, Database design")
        st.write("**Languages**: Java, Python, Hadoop")
        st.write("[GitHub Repository](https://github.com/your_project_link)")

        # Project 4: Flash Cards
        st.subheader("Flash Cards")
        st.write("Created a flashcard application using JavaFX with MVC architecture. Included sophisticated algorithms to manage card appearance and integrated user statistics for learning efficiency.")
        st.write("**Skills**: Data analysis, Database design, Object-oriented programming, MVC architecture, JavaFX, Statistics, Project management")
        st.write("**Languages**: Java")
        st.write("[GitHub Repository](https://github.com/your_project_link)")

        # Project 5: Projet Compilateur
        st.subheader("Projet Compilateur")
        st.write("Developed a Java-based compiler respecting formal language theory. Defined syntax and semantics for translating source to target languages, deepening knowledge of automata theory and syntax analysis.")
        st.write("**Skills**: Compiler design, Java, Formal languages, Automata theory, Syntax analysis, Project management")
        st.write("**Languages**: Java")
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

    else:
        # Project 1: Détection des Lésions Péri-apicales sur Radiographies Dentaires
        st.subheader("Détection des Lésions Péri-apicales sur Radiographies Dentaires")
        st.image("data/projects/Lesions.jpg")
        st.write("Developed an AI algorithm to detect peri-apical lesions in dental panoramic radiographs using convolutional neural networks (CNN) and YOLOv8 architecture. Achieved a remarkable 99% accuracy after extensive training and model optimization.")
        st.write("**Skills**: Deep learning, CNNs, YOLOv8, Computer vision, AI, Data Science, Project management, GitHub")
        st.write("**Languages**: Python, TensorFlow")
        st.write("[GitHub Repository](https://github.com/your_project_link)")
        

        # Project 2: Moteur de Recherche de Maladies et Médicaments
        st.subheader("Moteur de Recherche de Maladies et Médicaments")
        st.write("Built a machine learning model to classify geological facies using data from wells. Applied Random Forest and PCA using Scikit-learn, achieving 61.4% accuracy on complex geological data.")
        st.write("**Skills**: Data modeling, Random Forest, PCA, Data science, Project management, GitHub, Supervised learning")
        st.write("**Languages**: Python, Scikit-learn")
        st.write("[GitHub Repository](https://github.com/your_project_link)")

        # Project 3: Moteur de Recherche Médical
        st.subheader("Moteur de Recherche Médical")
        st.write("Developed a medical search engine with a JavaFX interface for identifying diseases and medications linked to symptoms. Used Hadoop and Apache for large-scale data management.")
        st.write("**Skills**: Big data, Hadoop, Apache Spark, JavaFX, Python, Data mapping, GitHub, Algorithms, Database design")
        st.write("**Languages**: Java, Python, Hadoop")
        st.write("[GitHub Repository](https://github.com/your_project_link)")

        # Project 4: Flash Cards
        st.subheader("Flash Cards")
        st.write("Created a flashcard application using JavaFX with MVC architecture. Included sophisticated algorithms to manage card appearance and integrated user statistics for learning efficiency.")
        st.write("**Skills**: Data analysis, Database design, Object-oriented programming, MVC architecture, JavaFX, Statistics, Project management")
        st.write("**Languages**: Java")
        st.write("[GitHub Repository](https://github.com/your_project_link)")

        # Project 5: Projet Compilateur
        st.subheader("Projet Compilateur")
        st.write("Developed a Java-based compiler respecting formal language theory. Defined syntax and semantics for translating source to target languages, deepening knowledge of automata theory and syntax analysis.")
        st.write("**Skills**: Compiler design, Java, Formal languages, Automata theory, Syntax analysis, Project management")
        st.write("**Languages**: Java")
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

