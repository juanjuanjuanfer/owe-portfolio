import streamlit as st
from streamlit_pdf_viewer import pdf_viewer


st.set_page_config(
    page_title="Assignment 4",
    page_icon=":four:",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""<div class="profile-container">
            <a href="portfolio">
        <button>Go Home 🏠</button>""", unsafe_allow_html=True)
st.markdown("## Assignment 4")
st.markdown("### Types of communication Report")
st.markdown("Due date: Sep 22nd, 2024")
st.markdown("### Instructions")
st.markdown("""
Write a report where you explain the characteristics of the types of human communication: 
- Intrapersonal, Interpersonal, Group, Collective, Massive, Simultaneous 

And distinguish the evolution, uses, scope and impact of human communication, assisted through technology:
 - Social networks, Virtual communities , Videoconferences


""")

st.markdown("## My work:")
pdf_path = "data/assignment4.pdf"
pdf_viewer(pdf_path, width=1000, height=2000)