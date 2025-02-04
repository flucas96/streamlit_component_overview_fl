import streamlit as st



from typing import Literal


heading_settings = {"font-size": 20, "font-weight": "bold"}

header_background_style = """
<style>
.header_background {
background-color: #f9f9f9;
border-radius: 2px;

}

@media (max-width: 768px) {
    .header_background {
        flex-direction: column; /* Stacks the elements vertically on small screens */
        justify-content: center; /* Centers the elements when stacked */
    }
}
</style>
"""

header_background_style_signal = """
<style>
.header_background_signal {
background-color: white;
border-radius: 10px;
border: 2px solid #1a3691; /* Defines a solid border with a specific color */
}

@media (max-width: 768px) {
    .header_background_signal {
        flex-direction: column; /* Stacks the elements vertically on small screens */
        justify-content: center; /* Centers the elements when stacked */
    }
}
</style>
"""


icon_style_header = """
<style>
.icon_heading {
position: absolute; 
left: 0;
padding-left:10px;
}
</style>
"""

icon_style_report_header = """
<style>
.icon_report_header {
font-size: 40px !important;
}
</style>
"""

icon_style_small_heading = """
<style>
.icon_small_heading {
font-size: 30px !important;
}
</style>
"""

icon_style_very_small_heading = """
<style>
.icon_very_small_heading {
font-size: 15px !important;
font-weight: bold;
}
</style>
"""

_font_very_small_header = """
<style>
.very_small_heading {
font-size: 20px !important;
font-weight: bold !important;
}

.very_small_header {
min-height: 40px;
margin-left: 5px;
margin-right: 5px;
}
</style>
"""

help_text_style = """
<style>
.help_text_container {
    display: flex;
    align-items: center;
    font-style: italic;
    border-bottom: 0.5px solid grey;
    color: grey;
}
.help_icon {
    font-size: 20px; /* Adjust the size of the icon as needed */
    margin-right: 15px; /* Adds some space between the icon and the text */
    margin-left: 5px;
}
</style>
"""

warning_text_style = """
<style>
.warning_text_container {
    display: flex;
    align-items: center;
    font-style: italic;
    border-bottom: 0.5px solid orange;
    color: orange;
}
.warning_icon {
    font-size: 20px; /* Adjust the size of the icon as needed */
    margin-right: 15px; /* Adds some space between the icon and the text */
    margin-left: 5px;
}
</style>
"""


logo_settings_style = """
<style>
.logo_settings {
    width: 200px;
    height: 200px;
    border: 2px solid #grey;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 10px;
    box-shadow: 0 0 10px grey;
    margin-top: 10px;
    border-radius: 20px;
}
.user_avatar {
    border-radius: 50%;
    width: 100%;
    height: 100%;
}
</style>
"""
form_label = """
<style>
.form_label {
    font-size: 18px;
    font-weight: bold;
    margin-bottom: 15px;
}
</style>
"""

section_header_style = """
    <style>
        .section_header {
            display: flex;
            align-items: center;
            width: 100%;
            padding: 10px;
            padding-left: 0px;
        }
        .section_header_text {
            /* Flexible item to not grow but align as per requirement */
            flex: none;
            text-align: ALIGN;
            font-weight:bold;
        }
        .section_header_line {
            /* Line that grows to fill space */
            flex-grow: 1;
            height: 0.5px;
            background-color: rgba(15, 41, 29, 0.2);
            margin-left: 10px; /* Space between text/icon and line */
    

        }
    </style>
    """

no_border_style = """
<style>
.no_border {
    border-bottom: none;
}
</style>
"""

produkt_logo_style = """
<style>
.product_logo {
    margin-bottom: 50px;
    height: 50px;
    transition: transform 0.2s;
    align-self: center !important;
}
</style>
"""

product_border_not_available = """
<style>
.product_logo_not_avaialble {
    border: 2px solid grey;
    padding: 5px;
    box-shadow: 0 0 5px grey;
}

.product_logo_not_avaialble:hover {
    box-shadow: 0 0 10px grey;
    transform: scale(1.05);
}
</style>
"""

product_border_available = """
<style>
.product_logo_avaialble {
    border: 5px solid #66B4AE;
    padding: 5px;
    box-shadow: 0 0 10px #66B4AE;
}

.product_logo_avaialble:hover {
    box-shadow: 0 0 20px #66B4AE;
    transform: scale(1.05);
}
</style>
"""

# css sytle to make img monochrom
monochrom_style = """
<style>
.monochrom {
    filter: grayscale(100%);
}
</style>
"""

quadrat_style = """
    <style>
    .quadrat {
        width: 40px;  /* Fixed width */
        height: 40px;  /* Fixed height */
        display: flex;
        justify-content: center;  /* Center horizontally */
        align-items: center;  /* Center vertically */
        margin-right: 10px;  /* Space between quadrats */
        padding: 10px;
        overflow: hidden;  /* Ensures text does not overflow */
        text-align: center;
        font-weight: bold;
    }
    .quadrat_available {
        border: 5px solid #66B4AE;
    }
    .quadrat_not_available {
        border: 2px solid grey;
    }

    .product_logo_container {
        display: flex;
        align-items: center; /* This ensures vertical center alignment */
    }
    .modul_container {
    margin-bottom: 50px;
    }
    </style>
    """



def display_info_border_left(
    text: str, space_above: int = 0, center: bool = False
) -> None:
    """
    Display custom HTML with border-left styling in a Streamlit app.

    Args:
        text (str): The text to be displayed within the styled HTML.
    """
    html_content = f"""
    <style>
        .border-left {{
            border-left: 2px solid #000;
            padding-left: 10px;
            margin: 10px 0;
            border-color: #44546A;
        }}
    </style>
    {"<br>" * space_above}
    {"<center>" if center else ""}
    <div class='border-left'>
        {text}
    </div>
    """

    st.html(
        html_content,
    )


def generate_header_report(title: str, icon: str = None):
    """
    Funktion um in Reports einen Header zu generieren mit Hintergrund etc.

    title = Text der im Header angezeigt werden soll
    icon = FontAweseome Icon zB "fa-regular fa-house"
    """

    st.markdown(header_background_style, unsafe_allow_html=True)
    if icon == None:
        st.markdown(
            f"""
                        <div class="header_background"><center><h1>{title}</h1></center></div>
                        """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(icon_style_header, unsafe_allow_html=True)
        st.markdown(icon_style_report_header, unsafe_allow_html=True)
        st.markdown(
            f"""
                        <div class="header_background" style="display: flex; align-items: center; justify-content: center;">
                        <i class="icon_report_header icon_heading fa {icon}" ></i>
                            <h1>{title}</h1>
                        </div>
                    """,
            unsafe_allow_html=True,
        )


def small_heading(title: str, icon: str = None, color: str = None):
    """
    Funktion um kleine Überschriften zu generieren
    """

    if icon == None:
        st.markdown(
            f"""<div class="header_background" style="display: flex; align-items: center; justify-content: center;"><h3>{title}</h3></div>""",
            unsafe_allow_html=True,
        )

    else:
        st.markdown(icon_style_small_heading, unsafe_allow_html=True)
        st.markdown(icon_style_header, unsafe_allow_html=True)
        st.markdown(
            f"""
                        <div class="header_background" style="display: flex; align-items: center; justify-content: center;">
                            <i class="icon_heading icon_small_heading fa {icon}" ></i>
                            <h3>{title}</h3>
                        </div>
                    """,
            unsafe_allow_html=True,
        )


def very_small_heading(title: str, icon: str = None):
    """
    Funktion um kleine Überschriften zu generieren
    """

    if icon == None:
        st.markdown(
            f"""<div class="header_background very_small_heading very_small_header">{title}</div>""",
            unsafe_allow_html=True,
        )

    else:
        st.markdown(icon_style_very_small_heading, unsafe_allow_html=True)
        st.markdown(icon_style_header, unsafe_allow_html=True)
        st.markdown(_font_very_small_header, unsafe_allow_html=True)
        st.markdown(
            f"""
                        <div class="header_background very_small_header" style="display: flex; align-items: center; justify-content: center;">
                            <i class="icon_heading icon_very_small_heading fa {icon}" ></i>
                            <span class="very_small_heading"><b>{title}</b></span>
                        </div>
                    """,
            unsafe_allow_html=True,
        )


def help_text(text: str, border: bool = True, icon: bool = True):
    """
    Funktion um Hilfetexte mit einem Info-Icon anzuzeigen.

    text: Der anzuzeigende Hilfetext.
    border: Ob ein unterstrichener Rand angezeigt werden soll.
    """
    # Define the CSS for the help text and the info icon

    # Render the CSS
    st.markdown(help_text_style, unsafe_allow_html=True)
    st.markdown(no_border_style, unsafe_allow_html=True)
    # Render the help text with the info circle icon
    st.html(
        f"""
                    <div class="help_text_container {"" if border else "no_border"}">
                        {'<i class="help_icon fa-regular fa-info-circle" ></i>' if icon  else ''}
                        <span>{text}</span>
                    </div>
                """,
    )


def add_line_break(num=1):
    st.markdown("<br>" * num, unsafe_allow_html=True)





def insert_form_label(text: str):
    """
    Funktion um die Labels in Formularen zu generieren
    """
    st.markdown(form_label, unsafe_allow_html=True)
    if text != None:
        st.markdown(f"""<div class="form_label">{text}</div>""", unsafe_allow_html=True)


def insert_section_header(
    text: str,
    icon: str = None,
    align: Literal["left", "center", "right"] = "left",
    font_size: int = 20,
    icon_color: str = "black",
    zusatz: str = None,
):
    """
    Inserts a section header with optional icon. The header text (and icon) can be aligned,
    and a horizontal line is added next to the text extending to the end of the container.

    Parameters:
    - text (str): The header text to display.
    - icon (str, optional): FontAwesome icon class for optional icon display next to the text.
    - align (str): Text alignment within the header ('left', 'right', 'center').
    """

    # Define the CSS for the section header

    # Inject the CSS style

    st.markdown(
        section_header_style.replace("ALIGN", align),
        unsafe_allow_html=True,
    )

    # Conditionally render icon if provided
    icon_html = (
        f"<i class='fa {icon}' style='color:{icon_color};'></i> " if icon else ""
    )

    if zusatz != None:
        zusatz_text = f"<span style='font-size: 16px; font-weight: normal; color: black; padding-left: 5px; font-style: italic'> {zusatz}</span>"
    else:
        zusatz_text = ""

    # Render the section header with text (and icon) and the horizontal line
    st.markdown(
        f"""
                    <div class="section_header">
                        <div class="section_header_text" style="font-size:{font_size}px;">{icon_html}{text}</div> {zusatz_text}
                        <div class="section_header_line"></div>
                    </div>
                """,
        unsafe_allow_html=True,
    )





def divider():
    st.markdown("<hr>", unsafe_allow_html=True)


def add_custom_space(height_px: int = 10):
    """
    Adds vertical space with a custom height specified in pixels.

    Parameters:
    - height_px (int): The height of the space in pixels.
    """
    st.markdown(
        f"""<div style="height: {height_px}px;"></div>""", unsafe_allow_html=True
    )



def warning_text(text: str, border: bool = True):
    """
    Funktion um Hilfetexte mit einem Info-Icon anzuzeigen.

    text: Der anzuzeigende Hilfetext.
    border: Ob ein unterstrichener Rand angezeigt werden soll.
    """
    # Define the CSS for the help text and the info icon

    # Render the CSS
    st.markdown(warning_text_style, unsafe_allow_html=True)
    st.markdown(no_border_style, unsafe_allow_html=True)
    # Render the help text with the info circle icon
    st.markdown(
        f"""
                    <div class="warning_text_container {"" if border else "no_border"}">
                        <i class="warning_icon fa-regular fa-triangle-exclamation" ></i>
                        <span>{text}</span>
                    </div>
                """,
        unsafe_allow_html=True,
    )





def write(
    text: str, font_size: int = 15, align: Literal["left", "center", "right"] = "left"
):
    """
    Funktion um eine leere Zeile zu generieren
    """

    st.markdown(
        f"""<div style="font-size: {font_size}px; text-align: {align};">{text}</div>""",
        unsafe_allow_html=True,
    )





def info_kasten(text: str):
    """
    Displays an information box with the given text.

    Parameters:
        text (str): The text to be displayed in the information box.

    Returns:
        None
    """
    with st.container(border=True):
        insert_section_header("Information", icon="fa-regular fa-info-circle")
        st.write(text, unsafe_allow_html=True)






def insert_card_with_image(image_path: str, content: str):
    """
    Funktion um eine Karte mit einem Bild und Text zu generieren (Beispiel Arbeitgeberstudie Selbstcheck)

    image_path: Pfad zum Bild (zb ./app/static/images/result_pic.jpeg)
    content: String mit dem Text der in der Karte angezeigt werden soll (gerne mit html)
    """

    html_template = (
        """
        <!DOCTYPE html>
    <html lang="de">
    <head>
        <meta charset="UTF-8">
        <title>Ihre Agentur-Befragung</title>
        <style>
        
            .content {
                line-height: 1.6;
                margin: 0;
                padding: 0;
                background: #f4f4f9;
                max-width: 800px;
                padding: 20px;
                background: #fff;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
                border-radius: 8px;
                border-collapse: collapse;
                border-color: #666;
            }
            .header-image_2 {
                width: 100%;
                height: 250px;
                background: url("""
        f'"{image_path}"'
        + """) no-repeat center center/cover;
                background-size: 100%; /* This zooms out the image */
                border-radius: 8px 8px 0 0;
            }
            .card_text {
                color: #666;
                margin: 20px 0;
                font-size: 17px;
            }
        </style>
    </head>
    <body>
        <div class="content">
            <div class="header-image_2"></div>
            <br><div class="card_text">"""
        + content
        + """
        </div></div>
    </body>
    </html>
        """
    )

    st.html(html_template)

