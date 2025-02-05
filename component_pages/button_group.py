import streamlit as st

import st_texte
from st_btn_group import st_btn_group
import base64
import pandas as pd
from io import BytesIO

def app():
    
    st_texte.generate_header_report("Button Group")
    
    st_texte.add_custom_space(20)
    st_texte.display_info_border_left("""
        <b>The main purpose of this component is to enable file downloads directly from Streamlit without triggering a rerun when clicking the button.</b> 
        Since developing this component, Streamlit has introduced a similar capability using <code>st.fragment</code> 
        in combination with <code>st.download_button()</code>. <b>However, I still prefer using this component because it offers greater styling flexibility.</b>
    """)
        

    
    st.markdown(
        """
        <a href="https://github.com/flucas96/st_btn_group" target="_blank">
        <img src="https://img.shields.io/github/stars/flucas96/st_btn_group?style=social" alt="GitHub stars">
        </a>
        """, unsafe_allow_html=True)
    
    st.markdown(
        """
        <a href="https://pypi.org/project/st-ant-st-btn-group/" trget="_blank">
        <img src="https://img.shields.io/pypi/v/st-btn-group" alt="PyPI version">
        </a>
        """, unsafe_allow_html=True)
    

    st_texte.insert_section_header("Installation & Import", icon="fa-solid fa-download")
    
    st.code("pip install st_btn_group")
    
    st.code("from st_btn_group import st_btn_group")
    
    st_texte.insert_section_header("Basic Usage", icon="fa-solid fa-code")
    
    col_left, col_right = st.columns(2)
    
    with col_left:
        shapes, sizes,align, disabled = st.columns((1,1,1,1,), vertical_alignment="center")
        merged, gap, divider = st.columns((1,1,1), vertical_alignment="center")
        shape = shapes.selectbox("**Shape**", ["default", "pill", "round", "circle", "square"], index=0)
        size = sizes.selectbox("**Size**", ["default", "large", "compact", "mini"], index=0)
        align = align.selectbox("**Align**", ["left", "center", "right"], index=0)
        disabled = disabled.checkbox("**Disabled**", value=False)

        merge_buttons = merged.checkbox("**Merge Buttons**", value=False)
        gap_between_buttons = gap.slider("**Gap between Buttons**", min_value=0, max_value=100, value=5)
        display_divider = divider.checkbox("**Display Divider**", value=False)


        buttons = [
            {   "label": "Button 1",
                "value": "1",
            },
            {   "label": "Button 2",
                "value": "2",
            },
            {   "label": "Button 3",
                "value": "3",
            },
        ]


        returned = st_btn_group(buttons=buttons, key="1", shape=shape, size=size, align=align, disabled= disabled, return_value=True, merge_buttons=merge_buttons, gap_between_buttons=str(gap_between_buttons), display_divider=display_divider)

        if returned:
            st.write("button clicked")

        st.write("Returned Value:", returned)

    with col_right:
        st.code("""
        buttons = [
        {   "label": "Button 1",
            "value": "1",
        },
        {   "label": "Button 2",
            "value": "2",
        },
        {   "label": "Button 3",
            "value": "3",
        },
        ]
        st_btn_group(buttons=buttons, key="1", shape='""" + shape + """', size='"""+ size + """', align ='"""+align+"""', disabled = """+str(disabled)+""" merge_buttons = """  +str(merge_buttons)+""", gap_between_buttons = """+str(gap_between_buttons) + """, display_divider = """+str(display_divider) + """, return_value = False)
        """
        , language="python")
        
        
    st_texte.insert_section_header("Advanced Usage")
    
    col_left, col_right = st.columns(2)
    with col_left:
        st_texte.very_small_heading("<b>Usage as Download Button</b>")
        
        st.write("It is possible to turn of the return value and use the button only as a download button. The advantage of this is that the app will not rerun when clicking the button.")

        data = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
        df = pd.DataFrame(data)
        buffer = BytesIO()
        df.to_excel(buffer, index=False, engine='openpyxl')
        buffer.seek(0)
        encoded_excel = base64.b64encode(buffer.getvalue()).decode('utf-8')
        
        button = [
    {   "startEnhancer": "<i class='fas fa-download'></i>",
        "label": "Download Excel",
        "download_file": {"data": encoded_excel, "filename": "Download.xlsx","large_file":False},
    },
]
        
        st_btn_group(buttons=button, key="download_button", return_value=False)
        
        st.code("""
    # Create a sample dataframe
    data = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
    df = pd.DataFrame(data)
    # Save the dataframe to an Excel file in memory
    buffer = BytesIO()
    df.to_excel(buffer, index=False, engine='openpyxl')
    buffer.seek(0)
    # Encode the Excel file as base64
    encoded_excel = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buttons = [{"startEnhancer": "<i class='fas fa-download'></i>",
            "label": "Download Excel",
            "download_file": {"data": encoded_excel, "filename": "test.xlsx"},},]
    st_btn_group(buttons=buttons, key="download_button", return_value=False)
    """, language="python")
        
        st.caption("When downloading larges dataframe it might be better for performace to set `large_file` to `True` in the `download_file` dict.")


    with col_right:
        st_texte.very_small_heading("<b>Adjust the Button Mode</b>")
        
        modes,_ = st.columns((1,1)) 
        mode = modes.selectbox("**Mode**", ["default", "checkbox", "radio"], index=0)
        st.caption("**Caution:** Change the mode in this demo might lead to weird outputs, because the button value is not reseted when the mode is changed")

        buttons = [
        {   "label": "Button 1",
            "value": "1",
        },
        {   "label": "Button 2",
            "value": "2",
        },
        {   "label": "Button 3",
            "value": "3",
        },
        {   "label": "Button 4",
            "value": "4",},
        {   "label": "Button 5",
            "value": "5",}
    ]


        returned = st_btn_group(buttons=buttons, key="2", mode=mode, return_value=True)
        st.write("Returned Value:", returned)

        st.code("""
    buttons = [
        {   "label": "Button 1",
            "value": "1",
        },
        {   "label": "Button 2",
            "value": "2",
        },
        {   "label": "Button 3",
            "value": "3",
        },
        {   "label": "Button 4",
            "value": "4",},
        {   "label": "Button 5",
            "value": "5",}
    ]
    returned = st_btn_group(buttons=buttons, key="2", mode='"""+mode+""", return_value=True)
    st.write("Returned Value:", returned)
    """, language="python")
