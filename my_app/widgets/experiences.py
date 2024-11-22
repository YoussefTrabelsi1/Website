import streamlit as st

def render_exp():
    # Experience Data
    experiences = [
        {
            "company": "SILAMIR GROUP",
            "role": "Consultant Data",
            "duration": "March 2024 - November 2024 (9 months)",
            "location": "Paris, Île-de-France, France",
            "responsibilities": [
                "Optimized Data Processes with dbt, Snowflake, and GitHub.",
                "Developed reusable data transformations in Snowflake using dbt.",
                "Automated data mapping with Python, reducing errors and enhancing workflows.",
                "Designed data pipelines for reliable dataset ingestion and transformation.",
                "Implemented centralized and scalable storage solutions with Snowflake.",
                "Collaborated via GitHub for version control and seamless teamwork.",
                "Automated PDF to Excel conversion scripts achieving 99% accuracy.",
                "Built a SAS code parser to analyze and optimize transformation processes.",
                "Created a dynamic Streamlit app for real-time metric visualization."
            ]
        },
        {
            "company": "Banque Populaire Grand Ouest",
            "role": "Assistant Engineer",
            "duration": "May 2023 - August 2023 (4 months)",
            "location": "Nantes, Pays de la Loire, France",
            "responsibilities": [
                "Industrialized and improved critical banking data quality processes.",
                "Automated data integration using Python and Bash scripts for CSV and Excel analysis.",
                "Created data visualizations with Matplotlib for clear and actionable insights.",
                "Used Visual Studio Code to maintain an efficient development environment.",
                "Enhanced banking data reliability, enabling informed decision-making."
            ]
        }
    ]

    # Streamlit Layout
    st.markdown(f'<h1 style="color: #3395c4;">Experiences :</h1>', unsafe_allow_html=True)
    for exp in experiences:
        st.subheader(f"{exp['role']} at {exp['company']}")
        st.write(f"**Duration:** {exp['duration']}")
        st.write(f"**Location:** {exp['location']}")
        st.write("**Key Responsibilities:**")
        for responsibility in exp['responsibilities']:
            st.write(f"- {responsibility}")
        st.markdown("---")
