import streamlit as st
import utils as utl
from views import home,about,configuration

st.set_page_config(layout="centered", page_title='Automated Data Analysis')
st.set_option('deprecation.showPyplotGlobalUse', False)
utl.inject_custom_css()
utl.navbar_component()

# Hiding footer
hide_default_format = """
           <style>
           footer {visibility: hidden;}
           </style>
           """
st.markdown(hide_default_format, unsafe_allow_html=True)

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

def navigation():
    route = utl.get_current_route()
    if route == "home":
        home.load_view()
    elif route == "about":
        about.load_view()
    elif route == "configuration":
        configuration.load_view()
    elif route == None:
        home.load_view()

navigation()