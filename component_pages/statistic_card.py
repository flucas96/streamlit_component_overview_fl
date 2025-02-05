import streamlit as st

import st_texte
from st_ant_statistic import st_ant_statistic

def app():
    
    st_texte.generate_header_report("Statistic Card")
    
    st_texte.add_custom_space(20)
    st_texte.display_info_border_left("<b>I needed a neat way to display statistics in Streamlit. Important to me was to be able to use HTML/ CSS styling to customize the look and feel of the statistic card.</b>")
    

    
    st.markdown(
        """
        <a href="https://github.com/flucas96/st_ant_statistic_component" target="_blank">
        <img src="https://img.shields.io/github/stars/flucas96/st_ant_statistic_component?style=social" alt="GitHub stars">
        </a>
        """, unsafe_allow_html=True)
    
    st.markdown(
        """
        <a href="https://pypi.org/project/st-ant-statistic/" trget="_blank">
        <img src="https://img.shields.io/pypi/v/st-ant-statistic" alt="PyPI version">
        </a>
        """, unsafe_allow_html=True)
    

    st_texte.insert_section_header("Installation & Import", icon="fa-solid fa-download")
    
    st.code("pip install st-ant-statistic")
    
    st.code("from st-ant-statistic import st-ant-statistic")
    
    st_texte.insert_section_header("Basic Usage", icon="fa-solid fa-code")
    
    col_left, col_right = st.columns(2)
    
    with col_left:
        loading_anmiation = st.checkbox("Loading Animation", value=False)
        loading_duration = st.slider("Loading Duration (in sec)", min_value=1, max_value=100, value=3)
        
        st_ant_statistic(
            title="My Statistic",
            value=150.243,
            prefix="<i class='fa fa-money' aria-hidden='true'></i>",
            precision=2,
            loadingAnimation=loading_anmiation,
            loadingDuration=loading_duration,
            decimalSeperator=",",
        )
        
        st.caption("You can define prefixes and suffixes. Font Awesome icons are supported out of the box.")
        
    with col_right:
        st.code(
            """
            st_ant_statistic(
                title="My Statistic",
                value=150.243,
                prefix="<i class='fa fa-money' aria-hidden='true'></i>",
                precision=2,
                loadingAnimation=loading_anmiation,
                loadingDuration=loading_duration,
                decimalSeperator=",",
            )
            """, language="python"
        )
        
    st_texte.insert_section_header("Advanced Usage")
    
    col_left, col_right = st.columns(2)
    with col_left:
        st_texte.very_small_heading("<b>Card Style</b>")
        
        card_border = st.checkbox("Card Border", value=False)
        card_hover = st.checkbox("Card Hover", value=True)
        st_ant_statistic(
            title="<center><b>My Statistic</b></center>",
            value=150.243,
            prefix="<i class='fa fa-money' aria-hidden='true'></i>",
            precision=2,
            decimalSeperator=",",
            card=True,
            card_bordered=card_border,
            card_hoverable=card_hover,
            cardStyle={"width":"95%", "background-color":"lightblue", "border-radius":"20px", "border-color":"black", "margin":"10px"},
            key="card",
            height=200,
            alignValue="center",
        )

        st.code("""
    st_ant_statistic(
        title="<center><b>My Statistic</b></center>",
        value=150.243,
        prefix="<i class='fa fa-money' aria-hidden='true'></i>",
        precision=2,
        decimalSeperator=",",
        card=True,
        card_bordered=card_border,
        card_hoverable=card_hover,
        cardStyle={"width":"95%", "background-color":"lightblue", "border-radius":"50px", "border-color":"black", "margin":"10px"},
        height=200,
        alignValue="center",
    )
    """, language="python")
        
        
    with col_right:
        st_texte.very_small_heading("<b>Custom Style</b>")


        col_left, col_right = st.columns((1,1))


        st_ant_statistic(
            title="<center><b>My Statistic</b></center>",
            value=100/3,
            prefix="<i class='fa fa-check' aria-hidden='true'></i>",
            precision=2,
            decimalSeperator=".",
            card=True,
            card_bordered=False,
            card_hoverable=True,
            cardStyle={"width":"95%", "background-color":"#f5f5f5", "border-radius":"10px", "border-color":"black", "margin":"10px"},
            key="custom",
            height=200,
            alignValue="center",
            titleStyle={"color":"red", "font-weight":"bold","font-size":"30px"},
            valueStyle={"color":"blue", "font-weight":"bold", "font-size":"30px"},
            loadingAnimation=True,
        )
        
        st.code("""
                 st_ant_statistic(
            title="<center><b>My Statistic</b></center>",
            value=100/3,
            prefix="<i class='fa fa-check' aria-hidden='true'></i>",
            precision=2,
            decimalSeperator=".",
            card=True,
            card_bordered=False,
            card_hoverable=True,
            cardStyle={"width":"95%", "background-color":"#f5f5f5", "border-radius":"10px", "border-color":"black", "margin":"10px"},
            key="custom",
            height=200,
            alignValue="center",
            titleStyle={"color":"red", "font-weight":"bold","font-size":"30px"},
            valueStyle={"color":"blue", "font-weight":"bold", "font-size":"30px"},
            loadingAnimation=True,
        )
                """)