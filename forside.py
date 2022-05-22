import streamlit as st
import requests
from streamlit_lottie import st_lottie


def load_lottie(url: str):
    r = requests.get(url)
    if r.status_code!= 200:
        return None
    return r.json()

def main():
    st_lottie(load_lottie('https://assets5.lottiefiles.com/packages/lf20_l22gyrgm.json'))  
    #--
    with st.sidebar:
        st.header('Nyttige lenker')
        c1, c2 = st.columns(2)
        with c1:
            st.write("[GRANADA](%s)" % "https://geo.ngu.no/kart/granada_mobil/")
            st.write("[Løsmasser](%s)" % "https://geo.ngu.no/kart/losmasse_mobil/")
            st.write("[NADAG](%s)" % "https://geo.ngu.no/kart/nadag-avansert/")
        with c2:
            st.write("[Berggrunn](%s)" % "https://geo.ngu.no/kart/berggrunn_mobil/")
            st.write("[InSAR](%s)" % "https://insar.ngu.no/")
            st.write("[AV-kartet](%s)" % "https://kart.asplanviak.no/")
        st.markdown("""---""")
        #--
        c1, c2 = st.columns(2)
        with c1:
            st.write("[Ebooks](%s)" % "https://asplanviak.sharepoint.com/sites/10333-03")
            st.write("[Gamle Ebooks](%s)" % "http://bikube/Oppdrag/8492/default.aspx")
            st.write("[GeoNorge](%s)" % "https://www.geonorge.no/")
        with c2:
            st.write("[UnderOslo](%s)" % "https://kart4.nois.no/underoslo/Content/login.aspx?standalone=true&onsuccess=restart&layout=underoslo&time=637883136354120798&vwr=asv")
            st.write("[Saksinnsyn](%s)" % "https://od2.pbe.oslo.kommune.no/kart/")
            st.write("[Nord Pool](%s)" % "https://www.nordpoolgroup.com/en/Market-data1/#/nordic/table")
        





  


