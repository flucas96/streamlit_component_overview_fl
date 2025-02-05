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
            "disabled": False,
        },
        
        {
            "label": "<b>Button Group</b>",
            "key": "6",
            "icon": "fa-solid fa-box",
            "disabled": False,

        },
        
        {
            "label": "<b>Antd Menu</b>",
            "key": "7",
            "icon": "fa-solid fa-list",
            "disabled": True,

            
        },
    ]
    
    
    #look into the query params if there is anything preselected
    defaultSelectedKeys = ["1"]
    defaultValue = []
    for key,value in st.query_params.to_dict().items():
        if key.lower() == "preselect":
            if value.lower() in [item["key"] for item in menu_structure]:
                defaultSelectedKeys = [str(value.lower())] 
                defaultValue = defaultSelectedKeys[0]
                st.session_state["main_menu"] = defaultSelectedKeys
                st.query_params.clear()
                break
            
            
                
    current_selection = st_ant_menu(
                        menu_structure,
                        key="main_menu",
                        multiple=False,
                       # css_styling_menu=css_styling,
                        additionalHeight=0,
                        iconSize=15,
                     #   generall_css_styling=general_style,
                        # defaultOpenKeys=expand_dashboard,
                        inlineIndent=10,
                        defaultSelectedKeys=defaultSelectedKeys,
                        defaultValue=defaultValue,
    )
    
 
    with st.sidebar:
        st.divider()
        
        st.html(
    """
    
    <div style="text-align: center;background-color:white;padding:20px;border-radius:10px;box-shadow: 0 0 10px #888;">
        <img src="https://avatars.githubusercontent.com/u/59033065" alt="Profile Picture" style="border-radius: 50%;width:170px;box-shadow: 0 0 0 0;">
        <h2 style="margin: 2px;">Fabian Lucas</h2>
        <h4 style="margin: 2px;"> Lead Data Analyst</h4> 
        <br>
        <p>👋 Hi, I'm Fabian Lucas. I am a passionate Streamlit developer. I hope you find my components useful.</p>
        <p>💡 Let's connect:</p>
        <a href="https://github.com/flucas96" target="_blank" style="text-decoration: none;">
            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" width="30">
        </a>
        <!-- LinkedIn -->
        <a href="https://www.linkedin.com/in/fabianlucas" target="_blank" style="text-decoration: none; margin-right: 10px;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" width="30">
        </a>
    </div>
    """,
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



if not current_selection: 
    current_selection = "1"
func_dict[str(current_selection)]()
        