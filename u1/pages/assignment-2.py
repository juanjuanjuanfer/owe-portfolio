import streamlit as st
from streamlit_pdf_viewer import pdf_viewer


st.set_page_config(
    page_title="Assignment 2",
    page_icon=":two:",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""<div class="profile-container">
            <a href="portfolio">
        <button>Go Home 🏠</button>""", unsafe_allow_html=True)
st.markdown("## Assignment 2")
st.markdown("### Fundamentals of the Communicative Process")
st.markdown("Due date: Sep 7th, 2024")
st.markdown("### Instructions")
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("""
    Explain the elements of the communicative process based on the Harold Lasswell and Manuel Castells models: 

    - Issuer 

    - Receiver 

    - Message 

    - Code 

    - Channel 

    - Feedback 

    - Context 

    - noise 
    """, unsafe_allow_html=True)
    
with c2:
    st.markdown("""
Explain the characteristics of the types of barriers and their bridges in the communication process: 

- Semantics 

- Physiological 

- Physics 

- Psychological 

- Techniques """, unsafe_allow_html=True)

with c3:
    st.markdown(""" 

Describe the purposes of the communication: 

- Report 

- Persuade 

- Entertain 



UPLOAD YOUR FILE AFTER THE PRESENTATION

""", unsafe_allow_html=True)
    
pdf_path = "data/assignment2.pdf"

st.markdown("## My work:")

pdf_viewer(pdf_path, width=1000, height=2000)