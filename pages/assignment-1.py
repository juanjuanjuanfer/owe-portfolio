import streamlit as st
from streamlit_pdf_viewer import pdf_viewer



st.set_page_config(
    page_title="Assignment 1",
    page_icon=":one:",
    layout="wide",
    initial_sidebar_state="collapsed"
)
st.markdown("""<div class="profile-container">
            <a href="portfolio">
        <button>Go Home 🏠</button>""", unsafe_allow_html=True)
st.markdown("## Assignment 1")
st.markdown("### We Both Reached for the Gun")
st.markdown("Due date: Sep 7th, 2024")
st.markdown("### Instructions")
st.markdown("""
After watching the video of Chicago's 'We Both Reached for the Gun' and answering the questions, upload your work here. 
            This activity will be completed on Friday, September 6th, during class time.""")
if st.button("Watch the video"):
    st.video("https://youtu.be/z5EZNPUJYXc?si=bfZwbjsD68xKzMDj")

pdf_path = "data/assignment1.pdf"

st.markdown("## My work:")

pdf_viewer(pdf_path, width=1000, height=2000)