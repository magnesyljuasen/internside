import streamlit as st
from datetime import datetime
import pandas as pd

from Fiberoptikk.standard_beregning import velg_konstanter, les_fil


def main():
    filer = st.file_uploader ('Last opp DTS-data', accept_multiple_files=True, key='DTS')
    if filer is not None:
        velg_konstanter()
        st.write("---")
        les_fil(filer)

        



            

main()

