import streamlit as st

def render_exp():
    # Experience Data
    experiences = [
        {
            "company": "SILAMIR GROUP",
            "role": "Data Consultant : Data Engineer",
            "duration": "February 2024 - December 2024 (11 months)",
            "location": "Paris, Île-de-France, France",
            "Description":"Designed and Depolyed an innovative data management solutions for a wealth management client via POCs using Snowflake, dbt and Python, optimizing business processes through automation and centralization of data flows.",
            "Skills":"Python | SQL | Snowflake | DBT | Azure Blob Storage | Pandas | Camelot | SAS | JSON | streamlit | Matplotlib",
            "responsibilities": [
                "Integrated into Azure Blob storage and transformed using Snowflake of 100 types of partner slips via Pandas and Camelot to centralize asset updates in 21 branches",
                "Built ELT/ETL pipelines with DBT to harmonize multi-source data and ensure historization of customer flows",
                "Standardized data from 100 partners via optimized SQL mapping scripts for internal agency dashboards, generating consolidated views",
                "Converted Excel, CSV and PDF files into standardized CSV files with a 99% success rate, improving ingestion into Snowflake",
                "Developed a Streamlit application generating reports through automated calculations and dynamic graphs",
                "Reduced loading time for complex queries by 50% using partitioning and indexing in Snowflake",
                "Integrated GPT-4 API for transcribing appointments and generating JSON-structured customer forms",
                "Developed a SAS parser in Python to identify key code structures for reliable and complete migrations",
                "Implemented an algorithm calculating the complexity of migrations from the parser results to accurately estimate the effort required",
                "Designed a Streamlit application for SAS project submission and visualization of dependencies via granular analysis",
                "Integrated dynamic graphics with Matplotlib and Pyplot to display complexity metrics and facilitate technical decision-making"


            ]
        },
        {
            "company": "CHR Metz-Thionville",
            "role": "AI Engineer / Data Scientist",
            "duration": "September 2023 - Febrauary 2024 (6 months)",
            "location": "Nancy, France",
            "Description":"Trained an AI model that uses YOLO layout and developed an automated training pipelines for medical image analysis, with a multi-model predictive interface and improved performance.",
            "Skills":"Python | AI | Yolo | DICOM ",
            "responsibilities": [
                "Optimized YOLO models, improving accuracy from 87% to 91%, reducing model size by 25% and accelerating processing to 7 seconds per file",
                "Created pipelines to automate DICOM data management and conversion, reducing preparation time by 40%",
                "Benchmarked three models (YOLO, U-Net, DETR) on 224 dental radiographs, achieving maximum accuracy of 99.9% with YOLO",
                "Developed a predictive multi-model Python interface with configurable logging system for performance monitoring and optimized maintenance",
            ]
        },
        {
            "company": "Banque Populaire Grand Ouest",
            "role": "Data Analyst / Data Engineer",
            "duration": "April 2023 - September 2023 (6 months)",
            "location": "Nantes, Pays de la Loire, France",
            "Description": "Developed data auditing scripts in Python/Shell and automation of large file processing to improve data quality and reduce processing times.",
            "Skills":"Python | Bash | Shell | Numpy | Pandas",
            "responsibilities": [
                "Created and optimized data audit scripts (Python, Shell) to compare, validate and audit customer CSV/Excel files",
                "Implemented descriptive calculations (Pandas, NumPy) to detect anomalies and reinforce data quality",
                "Reduced processing time for large files from 5 minutes to 10 seconds via optimized solutions in Shell/Python and Pandas",
                "Contributed to sprints and Scrum meetings to coordinate and prioritize tickets, tracking tasks and deliveries",
            ]
        }
        
    ]

    # Streamlit Layout
    st.markdown(f'<h1 style="color: #3395c4;">Experiences :</h1>', unsafe_allow_html=True)
    for exp in experiences:
        st.subheader(f"{exp['role']} at {exp['company']}")
        st.write(f"**Duration:** {exp['duration']}")
        st.write(f"**Location:** {exp['location']}")
        st.write(f"**Description:**")
        st.write(f"{exp['Description']}")
        st.write(f"**Skills:** {exp['Skills']}")
        st.write("**Key Responsibilities:**")
        for responsibility in exp['responsibilities']:
            st.write(f"- {responsibility}")
        st.markdown("---")
