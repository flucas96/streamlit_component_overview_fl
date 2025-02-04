import streamlit as st

import st_texte
from st_ant_tree import st_ant_tree
import json 

def app():
    
    st_texte.generate_header_report("Tree Select Component")
    
    st_texte.add_custom_space(20)
    st_texte.display_info_border_left("<b>This component offers the possibility to create a hierarchical selection inside Streamlit. Furthermore, it allows for HTML elements in the select options.</b>")
    

    
    st.markdown(
        """
        <a href="https://github.com/flucas96/st_ant_tree" target="_blank">
        <img src="https://img.shields.io/github/stars/flucas96/st_ant_tree?style=social" alt="GitHub stars">
        </a>
        """, unsafe_allow_html=True)
    
    st.markdown(
        """
        <a href="https://pypi.org/project/st-ant-tree/" trget="_blank">
        <img src="https://img.shields.io/pypi/v/st-ant-tree" alt="PyPI version">
        </a>
        """, unsafe_allow_html=True)

    st_texte.insert_section_header("Installation & Import", icon="fa-solid fa-download")
    
    st.code("pip install st-ant-tree")
    
    st.code("from st_ant_tree import st_ant_tree")
    
    st_texte.insert_section_header("Basic Usage", icon="fa-solid fa-code")
    
    col_left, col_right = st.columns(2)
    
    with col_left:
        tree_data = tree_data = [
    {
        "value": "germany",
        "title": """<b> Germany 🇩🇪 </b>""",
        "children": [
            {
                "value": "nrw",
                "title": "North Rhine-Westphalia",
                "children": [
                    {"value": "cologne", "title": "Cologne"},
                    {"value": "dusseldorf", "title": "Düsseldorf"},
                    {"value": "bonn", "title": "Bonn"},
                    {"value": "dortmund", "title": "Dortmund"},
                    {"value": "essen", "title": "Essen"},
                ],
            },
            {
                "value": "bavaria",
                "title": "Bavaria",
                "children": [
                    {"value": "munich", "title": "Munich"},
                    {"value": "nuremberg", "title": "Nuremberg"},
                    {"value": "augsburg", "title": "Augsburg"},
                    {"value": "regensburg", "title": "Regensburg"},
                ],
            },
            {
                "value": "hesse",
                "title": "<b> Hesse </b>",
                "children": [
                    {"value": "frankfurt", "title": "Frankfurt"},
                    {"value": "wiesbaden", "title": "Wiesbaden"},
                    {"value": "darmstadt", "title": "Darmstadt"},
                    {"value": "kassel", "title": "Kassel"},
                ],
            },
        ],
    },
    {
        "value": "france",
        "title": "<b> France 🇫🇷 </b>",
        "children": [
            {
                "value": "ile_de_france",
                "title": "Île-de-France",
                "children": [
                    {"value": "paris", "title": "Paris"},
                    {"value": "versailles", "title": "Versailles"},
                    {"value": "boulogne", "title": "Boulogne-Billancourt"},
                ],
            },
            {
                "value": "auvergne_rhone_alpes",
                "title": "Auvergne-Rhône-Alpes",
                "children": [
                    {"value": "lyon", "title": "Lyon"},
                    {"value": "grenoble", "title": "Grenoble"},
                    {"value": "saint_etienne", "title": "Saint-Étienne"},
                ],
            },
            {
                "value": "provence",
                "title": "Provence-Alpes-Côte d'Azur",
                "children": [
                    {"value": "marseille", "title": "Marseille"},
                    {"value": "nice", "title": "Nice"},
                    {"value": "cannes", "title": "Cannes"},
                ],
            },
        ],
    },
    {
        "value": "spain",
        "title": "<b> Spain 🇪🇸 </b>",
        "children": [
            {
                "value": "madrid_region",
                "title": "Madrid Region",
                "children": [
                    {"value": "madrid", "title": "Madrid"},
                    {"value": "alcala", "title": "Alcalá de Henares"},
                    {"value": "mostoles", "title": "Móstoles"},
                ],
            },
            {
                "value": "catalonia",
                "title": "Catalonia",
                "children": [
                    {"value": "barcelona", "title": "Barcelona"},
                    {"value": "girona", "title": "Girona"},
                    {"value": "tarragona", "title": "Tarragona"},
                ],
            },
            {
                "value": "andalusia",
                "title": "Andalusia",
                "children": [
                    {"value": "seville", "title": "Seville"},
                    {"value": "malaga", "title": "Málaga"},
                    {"value": "granada", "title": "Granada"},
                ],
            },
        ],
    },
]

    
    with col_right:
        with st.expander("**Tree Data Structure**", icon=":material/code:"):
            formatted_tree_data = json.dumps(tree_data, indent=4, ensure_ascii=False)

            st.code(formatted_tree_data, wrap_lines=True, language="json")
            
        
            
        st.code('''
                
    selected_values = st_ant_tree(treeData=tree_data)
    
    st.write("Selected Values: ",selected_values)                
    '''
                )


    with col_left:
        selected_values = st_ant_tree(treeData=tree_data)
        
        st.write("Selected Cities: ", selected_values)
        
        
    st_texte.insert_section_header("Advanced Usage", icon="fa-solid fa-code")
    
    col_1, col_2 = st.columns(2)
    
    with col_1:
        st_texte.very_small_heading("<b>Single Selection</b>")
        
        selected_values = st_ant_tree(treeData=tree_data, multiple=False, key="tree2", treeCheckable=False)
        
        st.write("Selected City: ", selected_values)
        
        st.code(
            """
            st_ant_tree(treeData=tree_data, multiple=False)
            """
        )
        

    with col_2:
        st_texte.very_small_heading("<b>Default Expanded Nodes</b>")
        
        selected_cities = st_ant_tree(treeData=tree_data, key="tree3", treeDefaultExpandedKeys=["spain"],)
        st.write("Selected Cities: ", selected_cities)
        st.code(
            """
            st_ant_tree(treeData=tree_data, treeDefaultExpandedKeys=["spain"])
            """, wrap_lines=True
        )
        
    col_1, col_2 = st.columns(2)

        
    with col_1:
        st_texte.very_small_heading("<b>Default Selected Nodes</b>")
        
        selected_cities = st_ant_tree(treeData=tree_data, key="tree4", defaultValue=["seville", "cologne"],)
        st.write("Selected Cities: ", selected_cities)
        st.code(
            """
            st_ant_tree(treeData=tree_data, defaultValue=["seville", "cologne"])
            """, wrap_lines=True
        )
        
    with col_2:
        st_texte.very_small_heading("<b>Disabled Nodes</b>")
        tree_data2 = tree_data.copy()
        tree_data2[0]["disabled"] = True
        st.caption("Add the disabled attribute to the node object you want to disable")
        
        selected_cities = st_ant_tree(treeData=tree_data2, key="tree5", )
        st.code(
            """
            tree_data[0]["disabled"] = True
            st_ant_tree(treeData=tree_data)
            """, wrap_lines=True
        )
        
        
    col_1, col_2 = st.columns(2)
    with col_1:
        st_texte.very_small_heading("<b>Custom CSS Styling</b>")
        
        st.caption("Make it look more like Streamlit")
        
                # Default theme settings
        primary_color = "#FF4B4B"
        background_color = "white"
        secondaryBackgroundColor = "rgb(248, 249, 251)"
        font_family = "sans-serif"


        # CSS with dynamic colors
        TREE_SELECTOR_CSS = f"""
        .ant-select {{
            padding: 0px;
            font-family: "{font_family}", sans-serif !important;
            line-height: 25.6px;
            font-size: 16px !important;
        }}

        .ant-select-selector {{
            padding-left: 8px !important;
            background-color: {secondaryBackgroundColor} !important;
            font-family: "{font_family}", sans-serif !important;
            border: 0px !important;
            min-height: 2.5rem;
            width: 100%; 
            display: flex; 
            flex-wrap: wrap;
            
        }}
        .ant-select-selection-placeholder {{
            color: rgba(49, 51, 63, 0.6) !important;
            font-family: "{font_family}", sans-serif !important;
            font-size: 1rem !important;
            font-weight: normal;
            line-height: 1.6;
            flex: inherit;
            white-space: nowrap;
            text-overflow: ellipsis;
            max-width: 100%;
            overflow: hidden;
            box-sizing: border-box;
        }}
        .ant-select.ant-select-disabled .ant-select-selection-placeholder {{
            color:  rgba(15, 41, 29, 0.3) !important;
        }}
        .ant-select.ant-select-disabled .ant-select-arrow {{
            color: rgba(15, 41, 29, 0.4) !important;
        }}

        .ant-select-selector:focus {{
            border: 2px solid {primary_color} !important;
        }}
        .ant-select-focused .ant-select-selector {{
            border: 2px solid {primary_color} !important;
        }}

        .ant-select .ant-select-arrow {{
            color: Black !important;
            font-size: 13px;
        }}

        .ant-select.ant-select-disabled .ant-select-selection-item {{
            background: rgba(15, 41, 29, 0.1) !important;
            
        }}

        .ant-select.ant-select-disabled .ant-select-selection-item-content {{
            cursor: not-allowed;
        }}

        .ant-select-selection-item {{
            background-color: {primary_color} !important;
            align-items: center;
            border-left-width: 0px;
            font-size: 14px;
            border-radius: 2px;
            padding: 0px 5px;
            color: {background_color}
        }}
        .ant-select-selection-overflow-item {{
            margin-right: 6px;
        }}
        .ant-select-selection-item-content {{
            font-weight: 500;
            text-overflow: ellipsis;
            white-space: nowrap;
            font-size: 15px;
            font-family: "{font_family}", sans-serif;
            text-size-adjust: 100%;
            cursor: pointer;
            vertical-align: 0.0em;
        }}
        .ant-select-selection-item-remove {{
            cursor: pointer;
            font-weight: 900;
        }}

        .ant-select-selection-item-remove .anticon-close svg {{
            width: 1.0em; 
            height: 1.0em; 
            vertical-align: 0.0em;
            color: {background_color}
        }} 

        .ant-select .ant-select-clear {{
            inset-inline-end: 35px;
            background-color: transparent;
            opacity: 10;
            width: 14px; 
            height: 14px; 
        }}
        .ant-select .ant-select-clear .anticon.anticon-close-circle {{
            color: #808495 !important;
            position: relative;
            vertical-align: 0.3em; 
        }}
        .ant-select .ant-select-clear .anticon.anticon-close-circle:hover {{
            color: black !important;  
        }}
        .ant-select-tree-switcher .anticon {{
        position: relative;
        top: -1.5px; 
        transform: translateY(-1.5px); 
        }}
        .ant-select-single .ant-select-selector .ant-select-selection-item {{
            background-color: #e6e9ef !important;
            color: black !important;
            align-content: center;
        }}

        .ant-tree-select-dropdown .ant-select-tree-checkbox-checked .ant-select-tree-checkbox-inner {{
            background-color: {primary_color};
            border-color: {primary_color};
        }}
        .ant-tree-select-dropdown .ant-select-tree-checkbox:hover .ant-select-tree-checkbox-inner {{
            background-color: #F0F2F6; 
        }}

        .ant-tree-select-dropdown .ant-select-tree-checkbox-wrapper:not(.ant-select-tree-checkbox-wrapper-disabled):hover .ant-select-tree-checkbox-inner,
        .ant-tree-select-dropdown .ant-select-tree-checkbox:not(.ant-select-tree-checkbox-disabled):hover .ant-select-tree-checkbox-inner {{
            border-color: grey;
        }}

        .ant-tree-select-dropdown .ant-select-tree-checkbox-wrapper-checked:not(.ant-select-tree-checkbox-wrapper-disabled):hover .ant-select-tree-checkbox-inner,
        .ant-tree-select-dropdown .ant-select-tree-checkbox-checked:not(.ant-select-tree-checkbox-disabled):hover .ant-select-tree-checkbox-inner {{
            background-color:  {primary_color};
            color: grey !important;
        }}
        .ant-tree-select-dropdown .ant-select-tree-checkbox-indeterminate .ant-select-tree-checkbox-inner:after {{
            background-color: {primary_color};
            color: grey !important;
        }}
        
        .ant-select-single .ant-select-selector .ant-select-selection-placeholder {{
        position: absolute;
        top: 50%;
        inset-inline-start: 11px;
        inset-inline-end: 11px;
        transform: translateY(-50%);
        transition: all 0.3s;
        }}
        .ant-select.ant-select-disabled .ant-select-selector .ant-select-selection-item {{
        color:  rgba(15, 41, 29, 0.3) !important;
        }}
        """

        st_ant_tree(treeData=tree_data, overall_css=TREE_SELECTOR_CSS, key="tree_selector")
        
        with st.expander("**Expand to see the CSS code**"):
            st.code(TREE_SELECTOR_CSS)
            
        st.code("st_ant_tree(treeData=tree_data, overall_css=TREE_SELECTOR_CSS)")