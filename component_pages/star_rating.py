import streamlit as st
import st_texte
from streamlit_star_rating import st_star_rating
def app():
    
    st_texte.generate_header_report("Star Rating Component")
    
    st_texte.add_custom_space(20)
    st_texte.display_info_border_left("<b>This component offers the possibility to add a star or emoji rating to you Streamlit app.</b>")
    

    
    st.markdown(
        """
        <a href="https://github.com/flucas96/streamlit_star_rating" target="_blank">
        <img src="https://img.shields.io/github/stars/flucas96/streamlit_star_rating?style=social" alt="GitHub stars">
        </a>
        """, unsafe_allow_html=True)
    
    st.markdown(
        """
        <a href="https://pypi.org/project/st-star-rating/" trget="_blank">
        <img src="https://img.shields.io/pypi/v/st-star-rating" alt="PyPI version">
        </a>
        """, unsafe_allow_html=True)
    
    
    st.markdown("""
                <a href="https://discuss.streamlit.io/t/new-component-star-ratings/36829" target="_blank">
    <img src="https://img.shields.io/badge/Streamlit%20Forum-Discussion-red?logo=streamlit" alt="Streamlit Forum Discussion">
    </a>
    """, unsafe_allow_html=True)

    st_texte.insert_section_header("Installation & Import", icon="fa-solid fa-download")
    
    st.code("pip install st_star_rating")
    
    st.code("from streamlit_star_rating import st_star_rating")
    
    st_texte.insert_section_header("Basic Usage", icon="fa-solid fa-code")
    
    col_left, col_right = st.columns(2)
    
    with col_left:
        stars = st_star_rating("", maxValue=5, defaultValue=3, key="rating")
        
        st.write("Selected Stars: ", stars)
        
    with col_right:
        st.code(
            """stars = st_star_rating("", maxValue=5, defaultValue=3, key="rating")"""
        )
        
    st_texte.insert_section_header("Advanced Usage")
    
    col_left, col_right = st.columns(2)
    with col_left:
        st_texte.very_small_heading("<b>Amount of Stars </b>")
        col_l, col_r = st.columns(2)
        nr_of_stars = col_l.slider("Number of stars", min_value=1, max_value=10, value=5)
        
        st_star_rating("", maxValue=nr_of_stars, defaultValue=0, key="rating2")
        
        st.code("""st_star_rating("", maxValue=nr_of_stars, defaultValue=0)""")
        
    with col_right:
        st_texte.very_small_heading("<b>Star Size </b>")
        col_l, col_r = st.columns(2)
        star_size = col_l.slider("Star Size", min_value=20, max_value=100, value=40)
        
        st_star_rating("", maxValue=5, defaultValue=0, key="rating3", size=star_size)
        
        st.code("""st_star_rating("", maxValue=5, defaultValue=0,starSize=star_size)""")
        
    col_left, col_right = st.columns(2)
    with col_left:
        st_texte.very_small_heading("<b>Use Emojis </b>")
        
        st_star_rating("", maxValue=5, defaultValue=0, key="rating4", emoticons=True)
        
        st.code("""st_star_rating("",  maxValue=5, defaultValue=0, key="rating4", emoticons=True)""")

    with col_right:
        st_texte.very_small_heading("Enable Reset Button")
        
        stars = st_star_rating("", maxValue=5, defaultValue=0, resetButton=True)
        st.write("Selected Stars: ", stars)
        st.code("""
                st_star_rating("", maxValue=5, defaultValue=0, resetButton=True)
                """)