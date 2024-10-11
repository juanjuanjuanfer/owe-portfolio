import streamlit as st
from PIL import Image
import streamlit.components.v1 as components


st.set_page_config(
    page_title="Portfolio",
    page_icon="⭐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for minimalist styling

# Header
st.markdown('<div class="custom-header">', unsafe_allow_html=True)
st.title("📚 Oral and Written Expression Portfolio")
st.header("Juan Antonio Fernandez Cruz")
c1, c2, c3 = st.columns(3)
with c1:
    # set button to show info
    if st.button("Unit I"):
        
        st.subheader("First Unit Assignments")
        st.markdown('</div>', unsafe_allow_html=True)

        # Brief introduction
        st.markdown("""
            Welcome to my portfolio of assignments for the Oral and Written Expression course. 
            This collection showcases my work and progress throughout the first unit.
        """)

        # Container for assignment buttons
        with st.container():
            st.markdown("### Browse Assignments")
            
            col1, col2 = st.columns(2)
            
            with col1:
                # go to assingment if clicked

                st.markdown("""<div class="profile-container">
            <a href="assignment-1">
        <button>📝 Assignment 1: "We both reached for the gun"</button>
            </a>""", unsafe_allow_html=True)
                st.markdown("""<div class="profile-container">
            <a href="assignment-2">
        <button>📝 Assignment 2: "Fundamentals of the communicative process"</button>
            </a>""", unsafe_allow_html=True)
                st.markdown("""<div class="profile-container">
            <a href="assignment-3">
        <button>📝 Assignment 3: "Types of communication video"</button>
            </a>""", unsafe_allow_html=True)
                st.markdown("""<div class="profile-container">
            <a href="assignment-4">
        <button>📝 Assignment 4: "Types of communication report"</button>
            </a>""", unsafe_allow_html=True)
                
            with col2:
                st.markdown("""<div class="profile-container">
            <a href="assignment-5">
        <button>📝 Assignment 5: "Classwork Sept 27th"</button>
            </a>""", unsafe_allow_html=True)
                st.markdown("""<div class="profile-container">
            <a href="assignment-6">
        <button>📝 Assignment 6: "Video: Communication in Real-world Situations"</button>
            </a>""", unsafe_allow_html=True)
                st.markdown("""<div class="profile-container">
            <a href="assignment-7">
        <button>📝 Assignment 7: "Summary: Introduction to an engineering report"</button>
            </a>""", unsafe_allow_html=True)
                st.markdown("""<div class="profile-container">
            <a href="assignment-8">
        <button>📝 Assignment 8: "Online Course"</button>
            </a>""", unsafe_allow_html=True)
with c2:
    if st.button("Unit II"):
        
        st.markdown("Not available yet")

with c3:
    if st.button("Unit III"):

        st.markdown("Not available yet")
# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #666;'>
        Juan Antonio Fernandez Cruz | 2109061@upy.edu.mx | Data 9A
    </div>
""", unsafe_allow_html=True)