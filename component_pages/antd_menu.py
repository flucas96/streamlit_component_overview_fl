import streamlit as st
import st_texte
from st_ant_menu import st_ant_menu
import numpy as np
import pandas as pd
import json
def app():
    
    st_texte.generate_header_report("Menu Component")
    
    st_texte.add_custom_space(20)
    st_texte.display_info_border_left("<b>This component is a implementation of the Ant Design Menu in Streamlit. It offers the possibility to create extendable menus and high level of customization. </b>")
    

    
    st.markdown(
        """
        <a href="https://github.com/flucas96/st_ant_menu/" target="_blank">
        <img src="https://img.shields.io/github/stars/flucas96/st_ant_menu?style=social" alt="GitHub stars">
        </a>
        """, unsafe_allow_html=True)
    
    st.markdown(
        """
        <a href="https://pypi.org/project/st-ant-menu/" trget="_blank">
        <img src="https://img.shields.io/pypi/v/st-ant-menu" alt="PyPI version">
        </a>
        """, unsafe_allow_html=True)
    
    
    # st.markdown("""
    #             <a href="https://discuss.streamlit.io/t/new-component-streamlit-mui-table/46025" target="_blank">
    # <img src="https://img.shields.io/badge/Streamlit%20Forum-Discussion-red?logo=streamlit" alt="Streamlit Forum Discussion">
    # </a>
    # """, unsafe_allow_html=True)

    st_texte.insert_section_header("Installation & Import", icon="fa-solid fa-download")
    
    st.code("pip install st_ant_menu")
    
    st.code("from st_ant_menu import st_ant_menu")
    
    st_texte.insert_section_header("Basic Usage", icon="fa-solid fa-code")
    
    col_left, col_right = st.columns(2)
    
    with col_left:
        menu_data = [
        {
            "label": "<b>Overview</b>",
            "key": "1",
            "icon": "fa-solid fa-house-chimney",
        },
        {"type": "divider"},

        { 
            "label": "<b>Tree Select</b>",
            "key": "2",
            "icon": "fa-solid fa-tree",
        },
        {
            "label": "<b>Star Rating</b>",
            "key": "3",
            "icon": "fa-solid fa-star",
        },
        
        {
            "label": "<b>MUI Table</b>",
            "key": "4",
            "icon": "fa-solid fa-table",
        },
        {
            "label": "<b> Statistic Card</b>",
            "key": "5",
            "icon": "fa-solid fa-chart-bar",
            "disabled": False,
        },
        {
            "label": "<b>Button Group</b>",
            "key": "6",
            "icon": "fa-solid fa-box",
            "disabled": False,
        },
            {"type": "divider"},
        
        {"label": "<b>More Information</b>", "key": "7", "icon": "fa-solid fa-list",
         "children": [
            {"label": "Github", "key": "8", "icon": "fa-brands fa-github"},
            {"label": "PyPi", "key": "9", "icon": "fa-brands fa-python"},
        ]},
        {"type": "divider"},
        {
            "label": "<b>Disabled Option</b>",
            "key": "7",
            "icon": "fa-solid fa-ban",
            "disabled": True,
        },
    ]

       
      
                                    
        #Text Style
        general_style = """
        .ant-menu {background-color: #f9f9f9 !important}
        .ant-menu-item {padding-top: 25px !important; padding-bottom: 25px !important; font-size: 15px !important}
        .ant-menu-submenu-title {padding-top: 25px !important; padding-bottom: 25px !important;}
        .ant-menu-submenu {padding-top: 5px !important}
        .ant-menu-submenu-title:hover {font-weight: bold !important}
        .ant-menu-item:hover {font-weight: bold !important;}
        """
        


        st_texte.add_custom_space(50)
        selected_option = st_ant_menu(
            menu_data, generall_css_styling=general_style, 
        )
        
        st.write("**Selected Option:** ", selected_option)
        
        st.write("This example showcases the possibitly to add dividers between menu items, creating nested menus and disabling options. View the 'Menu Data Structure' section to see how this menu was created.")
        st.write("Furthermore, it shows how to use CSS to style the menu as needed.")
    with col_right:
        with st.expander("**Menu Data Structure**", icon=":material/code:"):
            formatted_menu_data = json.dumps(menu_data, indent=4, ensure_ascii=False)

            st.code(formatted_menu_data, wrap_lines=True, language="json")
        st.code('''                   
        #Text Style
        general_style = """
        .ant-menu {background-color: #f9f9f9 !important}
        .ant-menu-item {padding-top: 20px !important; padding-bottom: 20px !important; font-size: 15px !important}
        .ant-menu-submenu-title {padding-top: 20px !important; padding-bottom: 20px !important;}
        .ant-menu-submenu {padding-top: 5px !important}
        .ant-menu-submenu-title:hover {font-weight: bold !important}
        .ant-menu-item:hover {font-weight: bold !important;}
        """
        selected_option = st_ant_menu(
            menu_data, generall_css_styling=general_style
        )
        
        st.write("**Selected Option:** ", selected_option)     
                ''')
        
    
    st_texte.insert_section_header("Advanced Usage")
    
    col_left, col_right = st.columns(2)
    with col_left:
        st_texte.very_small_heading("<b>Select Multiple Options</b>")
        st_texte.add_custom_space(20)
        selected_options = st_ant_menu(menu_data, key="menu2", multiple=True, generall_css_styling=general_style)
        
        st.write("**Selected Options:** ", selected_options)
        
        st.code("""
                selected_options = st_ant_menu(menu_data, key="menu2", multiple=True, generall_css_styling=general_style)

                """)
        
    with col_right:
        
        st_texte.very_small_heading("<b>Default Value</b>")
        st_texte.add_custom_space(20)
        selected_options = st_ant_menu(menu_data, key="menu3", multiple=False, generall_css_styling=general_style,
                                           defaultValue=["5"], defaultSelectedKeys=["5"])
        
        st.write("**Selected Option:** ", selected_options)
        
        st.code("""
                selected_options = st_ant_menu(menu_data, key="menu3", multiple=False, generall_css_styling=general_style,
                                           defaultValue=["5"], defaultSelectedKeys=["5"])

                """)
    col_left, col_right = st.columns(2)
    
    with col_left:
        st_texte.very_small_heading("<b>Default Expanded Menus</b>")
        st_texte.add_custom_space(20)
        selected_options = st_ant_menu(menu_data, key="menu4", multiple=False, generall_css_styling=general_style,
                                           defaultOpenKeys=["7"])
        
        st.write("**Selected Option:** ", selected_options)
        
        st.code("""
                selected_options = st_ant_menu(menu_data, key="menu4", multiple=False, generall_css_styling=general_style,
                                           defaultOpenKeys=["7"])

                """)
        st.write("It is possible to expand parent menus by default. The `defaultOpenKeys`parameter can be used to do this.")

  