import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

st.set_page_config(
    page_title="Assignment 5",
    page_icon=":five:",
    layout="wide",
    initial_sidebar_state="collapsed"
)


st.markdown("""<div class="profile-container">
            <a href="portfolio">
        <button>Go Home 🏠</button>""", unsafe_allow_html=True)
st.markdown("## Assignment 5")
st.markdown("### Classwork Sept 27th")
st.markdown("Due date: Sep 30th, 2024")
st.markdown("### Instructions")
st.markdown("No instructions for this assignment.")

pdf_path = "data/assignment5.pdf"

st.markdown("## My work:")
pdf_viewer(pdf_path, height=2000, width=1000)