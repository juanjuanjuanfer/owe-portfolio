import streamlit as st
from streamlit_pdf_viewer import pdf_viewer



st.set_page_config(
    page_title="Assignment 7",
    page_icon=":seven:",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""<div class="profile-container">
            <a href="portfolio">
        <button>Go Home 🏠</button>""", unsafe_allow_html=True)
st.markdown("## Assignment 7")
st.markdown("### Summary: Introduction to an engineering report")
st.markdown("Due date: Oct 7th, 2024")
st.markdown("### Instructions")
st.markdown("""
Make a summary of the following information, using references:
- https://www.gvsu.edu/cms4/asset/CC3BFEEB-C364-E1A1-A5390F221AC0FD2D/engineering_full_technical_report_gg_final.pdf 
- https://www.monash.edu/rlo/assignment-samples/engineering/eng-writing-technical-reports 
- http://www.sussex.ac.uk/ei/internal/forstudents/engineeringdesign/studyguides/techreportwriting 
- https://students.unimelb.edu.au/academic-skills/explore-our-resources/report-writing/technical-report-writing 

""")


st.markdown("## My work:")
pdf_path = "data/assignment7.pdf"
pdf_viewer(pdf_path, width=1000, height=2000)