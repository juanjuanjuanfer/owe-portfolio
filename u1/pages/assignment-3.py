import streamlit as st
from streamlit_pdf_viewer import pdf_viewer


st.set_page_config(
    page_title="Assignment 3",
    page_icon=":three:",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""<div class="profile-container">
            <a href="portfolio">
        <button>Go Home 🏠</button>""", unsafe_allow_html=True)
st.markdown("## Assignment 3")
st.markdown("### Types of communication Video")
st.markdown("Due date: Sep 19th, 2024")
st.markdown("### Instructions")
instructions = "data/instructions3.pdf"
pdf_viewer(instructions, width=1000, height=2000)



st.markdown("## My work:")
st.video("https://youtu.be/Ec7NIb4ACz4?si=jjtK9WUxQOi7Jac-")
