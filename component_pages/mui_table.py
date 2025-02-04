import streamlit as st
import st_texte
from st_mui_table import st_mui_table
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import random
def app():
    
    st_texte.generate_header_report("Material UI Table Component")
    
    st_texte.add_custom_space(20)
    st_texte.display_info_border_left("<b>This is a very simple implmentation of a Material UI Table in Streamlit. Main features are: <ul><li>  Rendering of HTML content in the table </li> <li> Possibility to expand rows </li> <li> Pagination </li> </ul></b>")
    

    
    st.markdown(
        """
        <a href="https://github.com/flucas96/st-mui-table/" target="_blank">
        <img src="https://img.shields.io/github/stars/flucas96/st-mui-table?style=social" alt="GitHub stars">
        </a>
        """, unsafe_allow_html=True)
    
    st.markdown(
        """
        <a href="https://pypi.org/project/st-mui-table/" trget="_blank">
        <img src="https://img.shields.io/pypi/v/st-mui-table" alt="PyPI version">
        </a>
        """, unsafe_allow_html=True)
    
    
    st.markdown("""
                <a href="https://discuss.streamlit.io/t/new-component-streamlit-mui-table/46025" target="_blank">
    <img src="https://img.shields.io/badge/Streamlit%20Forum-Discussion-red?logo=streamlit" alt="Streamlit Forum Discussion">
    </a>
    """, unsafe_allow_html=True)

    st_texte.insert_section_header("Installation & Import", icon="fa-solid fa-download")
    
    st.code("pip install st_mui_table")
    
    st.code("from st_mui_table import st_mui_table")
    
    st_texte.insert_section_header("Basic Usage", icon="fa-solid fa-code")
    
    col_left, col_right = st.columns(2)
    
    # Set a seed so the random values are the same each time you run the code
    np.random.seed(24)

    # Generate a list of random dates
    date_today = datetime.now()
    days = pd.date_range(date_today, date_today + timedelta(19), freq='D').strftime('%m/%d/%Y').tolist()

    # Generate a list of product names
    products = ['Product ' + str(i) for i in range(1, 6)]

    # Generate a DataFrame
    df = pd.DataFrame({
        'Date': days,
        'Product': [random.choice(products) for _ in range(20)],
        'Units Sold': [random.randint(1, 100) for _ in range(20)],
        'Unit Price': [round(random.uniform(10.5, 100.5), 2) for _ in range(20)]
    })


    # Calculate the Total Sales and add as a new column
    df['Total Sales'] = df['Units Sold'] * df['Unit Price']
    df["Total Sales"] =  df["Total Sales"].round(2)

    with col_left:

        st_mui_table(df,key="table1")

    with col_right:
        st.code("""
        st_mui_table(df)
        """, language="python")

        st.markdown("<b>Input Dataframe", unsafe_allow_html=True)
        st.dataframe(df)
        
    
    st_texte.insert_section_header("Advanced Usage")
    
    col_left, col_right = st.columns(2)
    with col_left:
        
        st_texte.very_small_heading("<b>HTML Content in the Table</b>")
        
        st.caption("It is possible to use whatever HTML inside the table. Just pass it through the dataframe as string and it will be rendered in the table. This can be used to add links, images, styling etc.")
        
        df["HTML Content"] = ["<a href='https://www.google.com'>Google</a>", "<img src='https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png' height='50'>"] * 10
        
        st_mui_table(df, key="table2")
        
        st.code("""
        df["HTML Content"] = ["<a href='https://www.google.com'>Google</a>", "<img src='https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png' height='50'>"] * 10
        st_mui_table(df)
        """, language="python", wrap_lines=True)
        
    with col_right:
        df2 = df.copy()
        st_texte.very_small_heading("<b>Expandable Rows</b>")
        
        detailColumns = st.multiselect("**Detail Columns**", df.columns, default=["Date", "Product"])
        detailColNum = st.slider("**Number of Detail Columns**", min_value=0, max_value=len(detailColumns), value=1)
        detailsHeader = st.text_input("**Details Header**", value="<b>Details</b>")
      

        for col in detailColumns:
            df2.rename(columns = {col:f"<b>{col}</b>"}, inplace = True)
        detailColumns = [f"<b>{col}</b>" for col in detailColumns]


        st_mui_table(df2,key="table4", detailColumns=detailColumns, detailColNum=detailColNum, detailsHeader=detailsHeader)
                
        st.code(f"""
        for col in detailColumns:
            df.rename(columns = {{col:f"<b>{{col}}</b>"}}, inplace = True)
        detailColumns = [f"<b>{{col}}</b>" for col in detailColumns]
        st_mui_table(df,key="table4", detailColumns={detailColumns}, detailColNum={detailColNum}, detailsHeader={detailsHeader})
        """, language="python")       
    col_left, col_right = st.columns(2)
    with col_left:
        st_texte.very_small_heading("<b>Row Selection</b>")
        
        selectedRow = st_mui_table(df, key="table5", return_clicked_cell=True)
        
        st.write("Selected Rows: ", selectedRow)
        
        st.code("""
                selectedRow = st_mui_table(df, key="table5", return_clicked_cell=True)
                """)
        
    with col_right:
        st_texte.very_small_heading("<b>Custom CSS Styling</b>")
    
    
        customCss = st.text_area("**Custom CSS**", value="""
        .MuiTableCell-root {
            border: 2px solid green;
        }
        """)

        paperCSS  = { "width": '100%',  "overflow": 'hidden',"paddingBottom": '1px', "border": '2px solid red'}

       
        st_mui_table(df,key="table6", customCss=customCss, paperStyle=paperCSS) 
        st.code("""
        paperCSS  = { "width": '100%',  "overflow": 'hidden',"paddingBottom": '1px', "border": '2px solid red'}
        st_mui_table(df2,key="table6", customCss={customCss}, paperStyle=paperCSS)
        """, language="python")
        
    
    st_texte.very_small_heading("More Features")
    
    col_left, col_right = st.columns((1,1))

    with col_right:

        pagination = st.checkbox("**Enable Pagination**", value=True)
        col1, col2 = st.columns((1,1))
        with col1:
            skipfirst = st.checkbox("**Skip to first Page Button**", value=True)
        with col2:
            skiplast = st.checkbox("**Skip to last Page Button**", value=True)
        pagination_label = st.text_input("**Pagination Label**", value="Rows per page",disabled= not pagination)
        minHeight = st.number_input("**Min Height**", value=200)
        max_heigth = st.number_input("**Max Height**", value=400,)
        if pagination:
            maxHeight = max_heigth
        else:
            maxHeight = max_heigth


        size = st.selectbox("**Size**", ["small", "medium"], index=1)
        padding = st.selectbox("**Padding**", ["normal", "checkbox", "none"], index=0)
        showHeaders = st.checkbox("**Show Headers**", value=True)
        stickyHeader = st.checkbox("**Sticky Header**", value=True)

        st.code(f"""
        st_mui_table(df2,key="table7", enablePagination={pagination}, size={size}, padding={padding}, showHeaders={showHeaders}, stickyHeader={stickyHeader}, maxHeight={maxHeight},
                    minHeight={minHeight}, paginationLabel={pagination_label}, showLastButtonPagination={skiplast}, showFirstButtonPagination={skipfirst})
        """, language="python", wrap_lines=True)

    with col_left:
        st_mui_table(df,key="table7", enablePagination=pagination, size=size, padding=padding, showHeaders=showHeaders, stickyHeader=stickyHeader,maxHeight=maxHeight,minHeight=minHeight,
                    paginationLabel=pagination_label, showLastButtonPagination=skiplast, showFirstButtonPagination=skipfirst)
