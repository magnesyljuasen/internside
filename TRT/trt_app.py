import streamlit as st
from datetime import datetime
import pandas as pd
import sys
sys.path.insert(0,'TRT')

from asplan_viak import Importer, Justeringer, Analyse, Plotting

def main():
    with st.sidebar:
        test_type = st.selectbox('Hvilken type test?', ('Asplan Viak', 'Seabrokers', 'Båsum'))
        fil = st.file_uploader ('Last opp testdata', key='TRT')
    if fil is not None:
        plotting = Plotting()
        #Asplan Viak
        if test_type == 'Asplan Viak':
            fil.name = 'AV.csv'
            importer = Importer(fil)
            df = importer.df

            with st.sidebar:
                dato = pd.Timestamp(st.date_input('Velg datoen testen ble startet:'))
            df = importer.test_data(dato)
            if df.shape[0] != 1:
                st.header('Rådata')
                plotting.enkel_graf(df)
                with st.expander('Data'):
                    st.write(df)

                st.header('Sirkulasjon')
                juster_data = Justeringer()
                df_sirkulasjon = juster_data.sirkulasjon(df)
                plotting.enkel_graf(df_sirkulasjon)
                with st.expander('Data'):
                    st.write (df_sirkulasjon)
                analyse_sirkulasjon = Analyse(df_sirkulasjon)
                st.metric('Uforstyrret temperatur fra sirkulasjon', str(analyse_sirkulasjon.gjennomsnittsverdi()) + ' °C')
                
                st.header('Varme')
                df_varme = juster_data.varme(df)
                plotting.enkel_graf(df_varme)
                with st.expander('Data'):
                    st.write (df_varme)




        #-----
        if test_type == 'Båsum':
            pass 

        """  """

