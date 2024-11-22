import streamlit as st

def render_education():
    # Education Data
    education = [
        {
            "institution": "TELECOM Nancy",
            "degree": "Engineer's degree, Artificial Intelligence and Big Data",
            "duration": "September 2021 - September 2024",
            "location": "Nancy, France",
            "description": "A specialized engineering degree focused on artificial intelligence and big data, emphasizing advanced analytics, machine learning, and data-driven decision-making."
        },
        {
            "institution": "IAE Nancy School of Management",
            "degree": "Master's degree, Business Administration and Management, General",
            "duration": "September 2023 - September 2024",
            "location": "Nancy, France",
            "description": "An advanced program in business administration, providing a comprehensive understanding of management principles, strategic planning, and organizational leadership."
        },
        {
            "institution": "ESPRIT (Ecole Supérieure Privée d'Ingénierie et de Technologies)",
            "degree": "Preparatory Classes for Elite Schools (CPGE), Mathematics and Physics",
            "duration": "September 2019 - March 2021",
            "location": "Tunis, Tunisia",
            "description": "A rigorous preparatory program focusing on mathematics and physics to prepare for competitive entrance exams to top-tier engineering and technical schools in France."
        },
    ]

    # Streamlit Layout
    st.title("Education")

    for edu in education:
        st.subheader(edu["degree"])
        st.write(f"**Institution:** {edu['institution']}")
        st.write(f"**Duration:** {edu['duration']}")
        st.write(f"**Location:** {edu['location']}")
        st.write(f"**Description:** {edu['description']}")
        st.markdown("---")
