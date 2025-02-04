import streamlit as st 

from st_ant_menu import st_ant_menu

import component_pages.overview
import component_pages.tree_select
import component_pages.star_rating
import component_pages.mui_table
import component_pages.statistic_card
import component_pages.button_group
import component_pages.antd_menu

st.set_page_config(page_title="Streamlit Component Overview", page_icon=":house:", layout="wide")


with st.sidebar:
    
    menu_structure = [
        {
            "label": "<b>Overview</b>",
            "key": "1",
            "icon": "fa-solid fa-house-chimney",
            
        },
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
        },
        
        {
            "label": "<b>Button Group</b>",
            "key": "6",
            "icon": "fa-solid fa-box",
        },
        
        {
            "label": "<b>Antd Menu</b>",
            "key": "7",
            "icon": "fa-solid fa-list",
            
        },
    ]
    
    
    #look into the query params if there is anything preselected
    defaultSelectedKeys = ["1"]
    for key,value in st.query_params.to_dict().items():
        if key.lower() == "preselect":
            if value.lower() in [item["key"] for item in menu_structure]:
                defaultSelectedKeys = [str(value.lower())] 
                
                st.query_params.clear()
                break
            
            
                
    
    current_selection = st_ant_menu(
                        menu_structure,
                        key="main_menu",
                        multiple=False,
                       # css_styling_menu=css_styling,
                        additionalHeight=0,
                        iconSize=20,
                     #   generall_css_styling=general_style,
                        # defaultOpenKeys=expand_dashboard,
                        inlineIndent=10,
                        defaultSelectedKeys=defaultSelectedKeys,
                        defaultValue=defaultSelectedKeys[0],
    )
    
    

func_dict = {
    "1": component_pages.overview.app,
    "2": component_pages.tree_select.app,
    "3": component_pages.star_rating.app,
    "4": component_pages.mui_table.app,
    "5": component_pages.statistic_card.app,
    "6": component_pages.button_group.app,
    "7": component_pages.antd_menu.app,
}




func_dict[current_selection]()
        