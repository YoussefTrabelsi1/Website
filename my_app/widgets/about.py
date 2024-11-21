import streamlit as st

def about_section(language):
    if language=="English":
        # Set the title of the app
    
        st.header("About me")
        
        # About text
        st.write("""
            Passionate about data and innovation, I'm a versatile profile with the ability to adapt quickly to new tools and 
            technologies. Always curious and motivated, I'm committed to taking on technical challenges and learning continuously 
            to meet the needs of ambitious projects. My aim is to contribute to dynamic teams while developing high value-added 
            solutions.
        """)
        
        # Display photo
        
        # CV Preview (just an example; link to a PDF or create your own preview)
        st.download_button("Download CV", "path_to_cv.pdf")
    else:
        
        st.header("À propos de moi")

        st.write("""Passionné par les données et l'innovation, je suis un profil polyvalent avec une capacité d'adaptation rapide à de 
        nouveaux outils et technologies. Toujours curieux et motivé, je m'engage à relever les défis techniques et à apprendre en 
        continu pour répondre aux besoins des projets ambitieux. Mon objectif est de contribuer à des équipes dynamiques tout en 
        développant des solutions à forte valeur ajoutée.""")
        # CV Preview (just an example; link to a PDF or create your own preview)
        st.download_button("Télécharger CV", "path_to_cv.pdf")
