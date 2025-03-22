import streamlit as st
from my_app.tools.display_projects import display_projects_streamlit

def render_projects():
    st.markdown('<h1 style="color: #3395c4;">Personal projects :</h1>', unsafe_allow_html=True)

    # Consolidated list of projects
    projects = [
        {
        'name': 'Online Retail ETL Pipeline & Analysis',
        'image_path': 'data/projects/OnlineRetail_ETL.png',  # You can create a simple diagram or screenshot as this image
        'problem_statement': 'The company needed to clean and analyze a year’s worth of transactional data to gain insights into customer behavior, supplier performance, and sales trends across regions.',
        'role': 'Designed a modular ETL pipeline using OOP principles; Implemented robust data cleaning with logging and unit tests; Processed business logic for supplier and continent-level analytics; Visualized insights in a Jupyter notebook.',
        'tools': 'Python, Pandas, Parquet, Matplotlib, Seaborn, Unittest, GitHub',
        'description': 'Built a full end-to-end ETL pipeline for an e-commerce dataset. Cleaned and transformed transactional data, enriched it with supplier and continent mapping, and saved it in optimized Parquet format. Conducted analysis in a notebook to uncover monthly trends, peak hours, top countries and products, and cancellation patterns.',
        },
        {
            'name': 'Detecting Periapical Lesions on Dental X-rays',
            'image_path': 'data/projects/Lesions.jpg',
            'problem_statement': 'Dental panoramic radiographs often fail to clearly reveal peri-apical lesions, leading to diagnostic errors. An AI-driven solution was needed to improve diagnostic accuracy.',
            'role': 'Designed and trained CNN models; Optimized YOLOv8 for object detection; Conducted extensive data preprocessing and testing; Managed project workflow and results analysis.',
            'tools': 'Python, TensorFlow, YOLOv8, Bash, GitHub',
            'description': 'Developed an AI algorithm to detect peri-apical lesions in dental panoramic radiographs using CNNs and YOLOv8 architecture. Achieved a remarkable 99% accuracy.',
        },
        {
        'name': 'Image Colorization using Generative Adversarial Networks (GAN) and U-Net',
        'image_path': 'data/projects/model_rows.png',
        'problem_statement': 'Grayscale images lack the rich color information needed for realistic visual interpretations. A robust AI approach was required to convert grayscale images into vivid and plausible color images, combining GANs for realistic data generation and U-Net for precise spatial feature extraction.',
        'role': 'Implemented a GAN-based colorization model using a U-Net architecture; Preprocessed and normalized 10,000 images from the COCO dataset; Trained the model using adversarial and L1 loss; Analyzed model performance, identified artifacts, and refined training strategies with GPU acceleration on Google Colab.',
        'tools': 'Python, TensorFlow/PyTorch, COCO Dataset, Google Colab, GPU Acceleration',
        'description': 'Developed a GAN-U-Net model to transform grayscale images into realistic colorized outputs. The approach involved extensive data preprocessing, training on 10,000 COCO images, and leveraging adversarial and L1 losses for quality optimization. Achieved improved realism and reduced artifacts through iterative refinement and GPU-based training acceleration.',
        },
        {
        'name': 'Protein Secondary Structure and Stability Prediction',
        'image_path': 'data/projects/Protein_Structure_Stability.webp',
        'problem_statement': 'Predicting protein secondary structures and their stability under mutations is a challenging bioinformatics task. An advanced machine learning approach, combined with tools like FoldX and RaSP, is needed to accurately model structural configurations and assess the impact of mutations.',
        'role': 'Analyzed and filtered a dataset of 643 human proteins based on pLDDT scores; Implemented FCN, CNN, and LSTM models to predict secondary structures with up to 88% accuracy; Assessed stability changes due to mutations (ddG) using classification and regression models; Integrated FoldX, RaSP, and neural networks to refine energy and structure predictions; Applied regularization techniques (Dropout, Early Stopping) to enhance model performance.',
        'tools': 'Python, TensorFlow/PyTorch, FoldX, RaSP, Neural Networks, Bioinformatics Toolkits',
        'description': 'Developed a comprehensive pipeline for predicting protein secondary structures and stability. Starting with a filtered set of 643 human proteins, multiple deep learning architectures (FCN, CNN, LSTM) achieved high prediction accuracy. Integration with FoldX and RaSP enabled precise stability and mutation analysis, while regularization methods improved overall model reliability and performance.',
        },
        {
        'name': 'Predictive Analysis and Visualization of Grenoble\'s Green Spaces',
        'image_path': 'data/projects/Grenoble_Green_Spaces.webp',
        'problem_statement': 'Urban green spaces require proactive management to maintain healthy vegetation and ensure sustainability. A predictive and interactive solution was needed to forecast tree defects, analyze the vegetation landscape, and support efficient maintenance strategies.',
        'role': 'Preprocessed and standardized temporal data; Performed categorical encoding and imputation of missing values; Implemented supervised classification models (RandomForest, AdaBoost) achieving 95% accuracy for uni-label classification; Developed an interactive map with dynamic filters and geographic coordinate conversion (EPSG 3945 to EPSG 4326); Applied the Apriori algorithm to discover association rules related to tree location and characteristics; Deployed a user interface combining interactive mapping with a centralized dashboard.',
        'tools': 'Python, Scikit-learn, GIS Libraries (e.g., GeoPandas), Apriori Algorithm, Web Frameworks for Visualization',
        'description': 'Designed a predictive and visual analytics platform for Grenoble’s green spaces. The approach integrated machine learning models, geospatial transformations, and association rule mining to identify tree defects and inform sustainable maintenance. A user-friendly, interactive interface and dashboard supported evidence-based decision-making for the city’s urban forestry management.'
        },
        {
        'name': 'NoSQL Platform for Protein Data Storage, Analysis, and Annotation',
        'image_path': 'data/projects/Protein_NoSQL_Platform.webp',
        'problem_statement': 'Protein data often comes in complex formats and requires flexible, scalable storage solutions. A NoSQL-based platform using MongoDB and Neo4j can efficiently handle complex queries, model protein relationships, and automate functional annotations for more accessible protein information.',
        'role': 'Implemented a document-based database (MongoDB) to store and query protein attributes; Constructed a relational protein graph in Neo4j to represent domain similarities and functional annotations; Developed a label-propagation algorithm for automatic annotation of unannotated proteins; Computed advanced metrics (e.g., Jaccard similarity), visualized protein neighborhoods, and provided statistical overviews.',
        'tools': 'MongoDB, Neo4j, Python, Neovis, D3.js',
        'description': 'Created a robust NoSQL platform that integrates MongoDB for complex data queries and Neo4j for graph modeling of protein relationships. The system automatically annotates protein functions through label propagation and offers advanced analytical features. Visualizations and similarity metrics support deeper insights into protein networks, streamlining access to functional protein data.'
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
        },
        


    ]

    # Display all projects
    display_projects_streamlit(projects)
