from logging import PlaceHolder
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('classic')
from os import listdir
from os.path import isfile, join
import math
import streamlit as st

def velg_konstanter():
    st.markdown("""---""")
    st.header('Fra borelogg')
    DYBDETILFJELL = st.number_input('Dybde til fjell', step=1)
    GRUNNVANNSTAND = st.number_input('Grunnvannstand', step=1)
    VANNINNSLAG = st.text_input('Vanninnslag', placeholder='[3, 10, 20]')
    st.markdown("""---""")
    st.header('Plotting')
    START = st.number_input('Startdybde', step=1)
    SLUTT = st.number_input('Sluttdybde', step=1, value=500)
    VARIGHET = st.number_input('Varighet', step=1, value=10)
    return DYBDETILFJELL, GRUNNVANNSTAND, VANNINNSLAG, START, SLUTT, VARIGHET

def les_fil(liste):
    for i, value in enumerate(liste):
        with open(value) as f:
                lines = f.readlines()

        temperaturListe = []
        dybdeListe = []

        for i in range (1, len (lines)):
            #Ta ut data 
            forrigeVerdi = lines [i - 1]
            data = lines [i]
            if forrigeVerdi == '<data\n' or forrigeVerdi == '   <data>\n' or forrigeVerdi == '<data>\n':
                splittetData = data.split (',')
                dybde = float (splittetData [0])
                dybdeListe.append (dybde)
                temperatur = splittetData [3]
                temperatur = float (temperatur.split() [0])
                temperaturListe.append (temperatur)
            #Finn tidspunkt og dato 
            if i == 10:
                splitter = data.split ('>') [1].split ('<') [0].split ('T')
                startDato = splitter [0]
                startKlokkeslett = splitter [1].split ('Z') [0].split ('.') [0]
            elif i == 11:
                splitter = data.split ('>') [1].split ('<') [0].split ('T')
                sluttDato = splitter [0]
                sluttKlokkeslett = splitter [1].split ('Z') [0].split ('.') [0]

        temperaturListe = np.array (temperaturListe)
        dybdeListe = np.array (dybdeListe)
        
        return dybdeListe, temperaturListe, startKlokkeslett, sluttKlokkeslett, startDato, sluttDato      


"""

def lesFil (fil):
    with open(fil) as f:
        lines = f.readlines()

    temperaturListe = []
    dybdeListe = []

    for i in range (1, len (lines)):
        #Ta ut data 
        forrigeVerdi = lines [i - 1]
        data = lines [i]
        if forrigeVerdi == '<data\n' or forrigeVerdi == '   <data>\n' or forrigeVerdi == '<data>\n':
            splittetData = data.split (',')
            dybde = float (splittetData [0])
            dybdeListe.append (dybde)
            temperatur = splittetData [3]
            temperatur = float (temperatur.split() [0])
            temperaturListe.append (temperatur)
        #Finn tidspunkt og dato 
        if i == 10:
            splitter = data.split ('>') [1].split ('<') [0].split ('T')
            startDato = splitter [0]
            startKlokkeslett = splitter [1].split ('Z') [0].split ('.') [0]
        elif i == 11:
            splitter = data.split ('>') [1].split ('<') [0].split ('T')
            sluttDato = splitter [0]
            sluttKlokkeslett = splitter [1].split ('Z') [0].split ('.') [0]

    temperaturListe = np.array (temperaturListe)
    dybdeListe = np.array (dybdeListe)
    
    return dybdeListe, temperaturListe, startKlokkeslett, sluttKlokkeslett, startDato, sluttDato

def rawPlot (dybdeListe, temperaturListe):
    #plt.style.use('seaborn-paper')

    #Plotting
    fig, ax = plt.subplots()
    x = dybdeListe
    y = temperaturListe
    ax.plot(x, y)

    #Grid, legend, limits og label 
    ax.set_title ('Filnavn: ' + '', fontsize = 14)
    ax.grid(True) 
    ax.set_ylim(.9 * min (temperaturListe), 1.1 * max (temperaturListe))
    ax.set_xlabel('Dybde [m]')
    ax.set_ylabel('Temperatur  [°C]')

def intervaller (dybdeListe, temperaturListe, start, slutt):
    for i in range (0, len(dybdeListe)):
        if int (dybdeListe [i]) == start:
            temperaturListe = np.delete (temperaturListe, range (0, i))
            dybdeListe = np.delete (dybdeListe, range (0, i))
            break 

    for i in range (0, len(dybdeListe)):
        if int (dybdeListe [i]) == slutt:
            temperaturListe = np.delete (temperaturListe, range (i, len (dybdeListe)))
            dybdeListe = np.delete (dybdeListe, range (i, len (dybdeListe)))
            break  
            
    return dybdeListe, temperaturListe

def varighetsGenerator (startTidspunkt, sluttTidspunkt, startDato, sluttDato):
    
    #Regn ut antall timer og antall minutter 
    antallTimer = int (sluttTidspunkt [0:2]) - int (startTidspunkt [0:2])
    antallMinutter = abs (int (sluttTidspunkt [3:5]) - int (startTidspunkt [3:5]))

    #Definer timer og minutter
    startTime = int (startTidspunkt [0:2])
    sluttTime = int (sluttTidspunkt [0:2])
    startMinutt = int (startTidspunkt [3:5])
    sluttMinutt = int (sluttTidspunkt [3:5]) 
        
    
    #Hvis sluttminutt er mindre enn startminutt
    if sluttMinutt > startMinutt:
        antallMinutter = sluttMinutt - startMinutt
        antallTimer = sluttTime - startTime
        
    #Hvis startminutt er større enn sluttminutt 
    elif sluttMinutt < startMinutt:
        antallMinutter = sluttMinutt + 60 - startMinutt
        antallTimer = sluttTime - startTime - 1
    
    #----------------------------------------------------------------
    #Dagskorrigering - fungerer bare for en dag - her må det utbedres
    if antallTimer < 0:
        antallTimer = startTime - abs(antallTimer)
        antallTimer = (24 - startTime) + antallTimer
    #----------------------------------------------------------------
    
    #Til timer + minutter
    varighet = antallTimer + (antallMinutter / 60)
    
    #Lag tekststreng
    varighetStr = str (antallTimer) + ' timer og ' + str (antallMinutter) + ' minutter'     
            
    return varighet, varighetStr

def limits (dybdeListe, temperaturListe, xminFaktor, xmaxFaktor):
    
    #Limits - x
    xmin = xminFaktor * min (temperaturListe)
    xmax = xmaxFaktor * max (temperaturListe)
    
    #Limits - y
    ymin = min (dybdeListe)
    ymax = max (dybdeListe)
    
    return xmin, xmax, ymin, ymax 

def plotter (dybdeListe, temperaturListe, startKlokkeslett, sluttKlokkeslett, startDato, varighet, varighetStr, navn, xmin, xmax, ymin, ymax):
    
    #Plotting
    fig, ax = plt.subplots()
    
    #Stil 
    plt.style.use('classic')
    
    #Plotting
    x = temperaturListe
    y = dybdeListe
    ax.plot(x, y, 'k')

    #Grid, legend og label 
    ax.set_title ('Tidspunkt: ' + str (startKlokkeslett) + ' - ' + str (sluttKlokkeslett) + '; ' + str (startDato) 
                  + '\n Varighet:' + varighetStr , fontsize = 12)
    ax.grid(True) 
    
    #Limits 
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    
    #Ticks
    ax.set_yticks(np.arange(min(y), max(y)+1, 10))
    
    #Labels
    ax.set_xlabel('Temperatur [°C]')
    ax.set_ylabel('Dybde [m]')
    
    #Invert - y
    ax.invert_yaxis()
    
    #Navngivning
    png = navn + '.png'
    svg = navn + '.svg'
    
    #Lagre filer 
    fig.savefig('Resultater\_' + png)
    fig.savefig('Resultater\_' + svg, format = 'svg', dpi = 1200)
    
    plt.close (fig)


def alt_i_ett_plotter (dybdeListe, temperaturListe, startKlokkeslett, sluttKlokkeslett, startDato, varighet, varighetStr, navn, xmin, xmax, ymin, ymax, fig, ax, index):
    #Stil 
    #plt.style.use('classic')
    n = 10
    colors = plt.cm.rainbow(np.linspace(0, 1, n))

    #Plotting
    x = temperaturListe
    y = dybdeListe
    ax.plot(x, y, label = varighetStr, color = colors [(n-1) - index], linewidth=0.5)

    plt.legend(loc = 'best', prop={'size': 6})

    #Grid, legend og label 
    ax.grid(True) 
    
    #Limits 
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    
    #Ticks
    ax.set_yticks(np.arange(min(y), max(y)+1, 10))
    
    #Labels
    ax.set_xlabel('Temperatur [°C]')
    ax.set_ylabel('Dybde [m]')
    
    #Invert - y
    ax.invert_yaxis()
    




#def lagGif (GIF_NAVN, alleFilnavn):
    
#    filListe = range (1, len (alleFilnavn) + 1)
#    filListeStr = [str(x) for x in filListe]
#    filListeStrNy = []
#    for i in range (0, len (filListeStr)):
#        f = filListeStr [i] + '.png'
#        filListeStrNy.append (f)

#    # Build GIF
#    with imageio.get_writer(GIF_NAVN, mode='I') as writer:
#        bilde = 0
#        for filename in filListeStrNy:
#            try:
#                image = imageio.imread('Resultater\_' + filename)
#                bilde = 1
#            except:
#                print ('Ikke noe bilde')
#
#            if bilde == 1:
#                writer.append_data(image)

def round_nearest(n, r):
    return n - math.fmod(n, r)

def main ():
    
    #Initialiser konstanter
    START, SLUTT, VARIGHET, GIF_NAVN, FILPLASSERING, xminFaktor, xmaxFaktor, DYBDETILFJELL, GRUNNVANNSTAND, VANNINNSLAG = konstanter ()
    
    #Åpne alle filer
    alleFilnavn = [f for f in listdir(FILPLASSERING) if isfile(join(FILPLASSERING, f))]
    
    #For hver enkelt fil
    varighet = 0
    dag = 0
    j = 0
    fig1, ax1 = plt.subplots()
    for i in range (0, len (alleFilnavn)):
        #Les fil
        filnavn = alleFilnavn [i]
        fil = FILPLASSERING + '\\' + filnavn
        try: 
            dybdeListe, temperaturListe, startKlokkeslett, sluttKlokkeslett, startDato, sluttDato = lesFil (fil)
        except:
            print ("Tom fil")
            

        #Sett starttidspunkt for første fil og sluttidspunkt for siste fil
        if i == 0:
            startTidspunkt = startKlokkeslett
        sluttTidspunkt = sluttKlokkeslett 
        startTidspunkt

        #Beregn varighet
        forrige_varighet = varighet
        varighet, varighetStr = varighetsGenerator (startTidspunkt, sluttTidspunkt, startDato, sluttDato)
        neste_varighet = varighet
        
        if neste_varighet < forrige_varighet: 
            dag += 1
        
        korrigertVarighet = varighet + dag * 24
        
        if korrigertVarighet > VARIGHET:
            break 
        
        #Lag tekststreng
        #korrigertVarighetStr = str (math.floor (korrigertVarighet)) + ' timer og ' + str (int ((korrigertVarighet - (math.floor (korrigertVarighet)))*60)) + ' minutter' 
        korrigertVarighetStr = str (math.floor (korrigertVarighet)) + ' timer'
        
        #Velg fra dybde til dybde
        dybdeListe, temperaturListe = intervaller (dybdeListe, temperaturListe, START, SLUTT)
        
        #Skaler dybder
        dybdeListe = dybdeListe - dybdeListe [0]
        
        #Sett limits for plotting, for graf 1 
        if i == 0:
            xmin, xmax, ymin, ymax = limits (dybdeListe, temperaturListe, xminFaktor, xmaxFaktor)
            xmin = 7
            xmax = 14

        opplsn = 0.1
        #if round_nearest (korrigertVarighet, opplsn) == 70 or round_nearest (korrigertVarighet, opplsn) == 71 or round_nearest (korrigertVarighet, opplsn) == 72 or round_nearest (korrigertVarighet, opplsn) == 73 or round_nearest (korrigertVarighet, opplsn) == 74 or round_nearest (korrigertVarighet, opplsn) == 75:        
        if round_nearest (korrigertVarighet,0.1) == j:
            alt_i_ett_plotter(dybdeListe, temperaturListe, startKlokkeslett, sluttKlokkeslett, startDato, korrigertVarighet, korrigertVarighetStr, str (i), xmin, xmax, ymin, ymax, fig1, ax1, j)
            j += 1

        if round_nearest (korrigertVarighet, opplsn) == 0 or round_nearest (korrigertVarighet, opplsn) == 1 or round_nearest (korrigertVarighet, opplsn) == 2 or round_nearest (korrigertVarighet, opplsn) == 3 or round_nearest (korrigertVarighet, opplsn) == 4 or round_nearest (korrigertVarighet, opplsn) == 5 or round_nearest (korrigertVarighet, opplsn) == 10 or round_nearest (korrigertVarighet, opplsn) == 30 or round_nearest (korrigertVarighet, opplsn) == 50 or round_nearest (korrigertVarighet, opplsn) == 68 or round_nearest (korrigertVarighet, opplsn) == 69 or round_nearest (korrigertVarighet, opplsn) == 70 or round_nearest (korrigertVarighet, opplsn) == 71 or round_nearest (korrigertVarighet, opplsn) == 72 or round_nearest (korrigertVarighet, opplsn) == 73 or round_nearest (korrigertVarighet, opplsn) == 74 or round_nearest (korrigertVarighet, opplsn) == 75:
        #if round_nearest (korrigertVarighet, opplsn) == 70 or round_nearest (korrigertVarighet, opplsn) == 71 or round_nearest (korrigertVarighet, opplsn) == 72 or round_nearest (korrigertVarighet, opplsn) == 73 or round_nearest (korrigertVarighet, opplsn) == 74 or round_nearest (korrigertVarighet, opplsn) == 75:
            plotter (dybdeListe, temperaturListe, startKlokkeslett, sluttKlokkeslett, startDato, korrigertVarighet, korrigertVarighetStr, str (i), xmin, xmax, ymin, ymax)

    #plt.axhline(y=GRUNNVANNSTAND, color='r', linestyle='-',label='Grunnvannstand fra borelogg')
    #plt.axhline(y=DYBDETILFJELL, color='r', linestyle='-', label='Dybde til fjell fra borelogg')
    #plt.axhline(y=VANNINNSLAG, color='r', linestyle='-', label='Vanninnslag fra borelogg')
    plt.close (fig1)
    fig1.savefig('Resultater\_' + '.png', format = 'png', dpi = 1200)
    #Lag GIF
    #lagGif (GIF_NAVN, alleFilnavn)


main ()
"""