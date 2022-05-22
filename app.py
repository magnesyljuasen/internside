import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image


import forside
from TRT import trt_app
from Fiberoptikk import fiberoptikk_app
from Kart import kart_app
from Rapportmaler import rapport_app


def main():
    #--Forside--
    col1, col2, col3 = st.columns(3)
    with col1:
        image = Image.open('logo.png')
        st.image(image)  
    with col2:
        st.title("Internside")
        st.write('Grunnvarme')
    #--Forside--
    app = option_menu(None, ['Hjem', 'TRT', 'DTS', 'Kart', 'Maler'], 
    icons=['house', 'graph-up', "calculator", 'geo-alt', 'file-earmark-text'], 
    menu_icon="app", default_index=0, orientation="horizontal")
    
    if app == 'Hjem':
        forside.main()
    if app == 'TRT':
        trt_app.main()
    if app == 'DTS':
        pass
        #fiberoptikk_app.main()
    if app == 'Kart':
        kart_app.main()
    if app == 'Maler':
        rapport_app.main()


main()

