import streamlit as st

import st_texte
def app():
    
    st_texte.generate_header_report("Welcome!")
    
    st_texte.add_custom_space(20)
    st_texte.display_info_border_left("""
    <div style="font-family: Arial, sans-serif; line-height: 1.6; text-align: justify;">
        <b>Using Streamlit daily in a professional context for the last three years</b>, I have encountered several instances where I needed a bit more functionality. <br><br>
        
        Often, Streamlit offered too little customizability to perfectly meet the client's needs. Because of this, I explored creating my own Streamlit components to extend its functionality. <br><br>
        
        The first component I developed was the <b>Star Rating</b> component. Its main purpose was to help me learn how to use React and TypeScript to create a component and publish it on PyPI. <br><br>
        
        Since then, I have created several more components, each designed to address one or more specific shortcomings I encountered in Streamlit at the time. Feel free to explore them using the menu on the right—<i>(which, by the way, is also a custom component 😉)</i>.
    </div>
""")

    st_texte.insert_section_header("Overview", icon="fa-solid fa-download")
    
    
    
    st_texte.small_heading("Star Rating")
    st_texte.add_custom_space(20)
    col_l, col_r = st.columns(2)

    with col_l:
        st.write("As mentioned in the introduction, this was the first component I developed, and it helped me better understand how Streamlit components work.")
        st.write("It adds functionality to Streamlit by allowing users to provide input through a star rating system.")

        st.link_button("**View the component**", url="/?preselect=3", type="primary", icon=":material/star:")

    with col_r:
        st.image("./static/images/star_rating.png")
        
    st_texte.add_custom_space(20)

    st_texte.small_heading("Tree Select")
    
    st_texte.add_custom_space(20)
    

    col_l, col_r = st.columns(2)
    with col_l:
        st.write("The tree selection component is based on an Ant Design React component. I needed a way to create hierarchical selections in Streamlit because I had many options that required structure. Additionally, I wanted the ability to style the options using HTML (e.g., bold text, different colors, etc.) to enhance the user experience.")
        st.link_button("**View the component**", url="/?preselect=2", type="primary", icon=":material/park:")

    with col_r:
        st.image("./static/images/tree_selector.png")
        
        
    st_texte.small_heading("MUI Table")
    
    st_texte.add_custom_space(20)
    col_l, col_r = st.columns(2)
    
    with col_l:
        st.write("I needed a way to expand table rows to display additional information. Additionally, the ability to render HTML within the table is highly useful, as it allows me to include links, images, styling, and more.")
        
        st.link_button("**View the component**", url="/?preselect=4", type="primary", icon=":material/table:")
        
    with col_r:
        st.image("./static/images/mui_table.png")
    