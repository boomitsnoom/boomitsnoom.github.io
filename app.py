import streamlit as st
from PIL import Image
from info import *
from static import *
import streamlit.components.v1 as components
from pages import about_me, contact, education, projects, skills

st.set_page_config(page_title='Naum Markenzon\'s Portfolio' ,layout="wide")
output_container = st.empty()
total_output_container = st.container()

with st.sidebar:
    components.html(linkedin['badge'],height=300)
    option = st.selectbox(
     '',
     ('All','About Me', 'Education', 'Skills', 'Projects','Contact'))
    if option == 'All':
        about_me.write_about_me(total_output_container)
        education.write_education(total_output_container)
        skills.write_skills(total_output_container)
        projects.write_projects(total_output_container)
        contact.write_contact(total_output_container)
    elif option == 'About Me':
        about_me.write_about_me(output_container)
    elif option == 'Education':
        education.write_education(output_container)
    elif option == 'Skills':
        skills.write_skills(output_container)
    elif option == 'Projects':
        projects.write_projects(output_container)
    elif option == 'Contact':
        contact.write_contact(output_container)
#st.session_state



# with st.expander("About Me") as about_me_c:
#      st.write(personal_info["bio"],expanded=True)
