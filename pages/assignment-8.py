import streamlit as st
from streamlit_pdf_viewer import pdf_viewer


st.set_page_config(
    page_title="Assignment 8",
    page_icon=":eight:",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""<div class="profile-container">
            <a href="portfolio">
        <button>Go Home 🏠</button>""", unsafe_allow_html=True)
st.markdown("## Assignment 8")
st.markdown("### Online Course")
st.markdown("Due date: Oct 13th, 2024")
st.markdown("### Instructions")
st.markdown("Upload your certificate")

pdf_path = "data/certificate.pdf"

st.markdown("## My work:")
pdf_viewer(pdf_path, width=1000, height=2000)