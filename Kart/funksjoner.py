#from folium.folium import Map
#from IPython.display import HTML

#def inline_map(m):
#    if isinstance(m, Map):
#        m._build_map()
#        srcdoc = m.HTML.replace('"', '&quot;')
#        embed = HTML('<iframe srcdoc="{srcdoc}" '
#                     'style="width: 100%; height: 500px; '
#                     'border: none"></iframe>'.format(srcdoc=srcdoc))
#    else:
#        raise ValueError('{!r} is not a folium Map instance.')
#    return embed




#    response = requests.get('https://geo.ngu.no/mapserver/BerggrunnN50WMS2?request=GetCapabilities&SERVICE=WMS')
#    st.write(response)

#    st.title ('AV Grunnvarme - Kart')
#    st.markdown("""---""")

#    wms = WebMapService('https://geo.ngu.no/mapserver/BerggrunnN50WMS2?request=GetCapabilities&SERVICE=WMS')
#    print("Title: ", wms.identification.title)
#    print("Type: ", wms.identification.type)
#    print("Operations: ", [op.name for op in wms.operations])
#    print("GetMap options: ", wms.getOperationByName('GetMap').formatOptions)
#    a = wms.contents.keys()
#    for key in a:
#        print(wms.contents[key].title)
#    
    #--
#    name = key
#    layer = wms.contents[name]
#    print("Abstract: ", layer.abstract)
#    print("BBox: ", layer.boundingBoxWGS84)
#    print("CRS: ", layer.crsOptions)
#    print("Styles: ", layer.styles)
#    print("Timestamps: ", layer.timepositions)
#    HTML(layer.parent.abstract)

        #--
#    response = wms.getmap(layers=[name,],
#                    styles=['default'],
#                    bbox=(0, 10, 40, 50), # Left, bottom, right, top
#                    format='image/jpeg',
#                    size=(600,600),
#                    srs='EPSG:4326',
#                    #time='2018-09-16',
#                    transparent=True)

#    print(type(response))

#    out = open('jpl_mosaic_visb.jpg', 'wb')
#    out.write(response.read())
#    out.close()

#    m = Map(location=[63,5], zoom_start=5, tiles=None)
#    folium.WmsTileLayer('https://kart.dirmin.no/dirmin/services/GruvesikringsregisterBeta/MapServer/WmsServer?request=GetLegendGraphic%26version=1.1.1%26format=image/png%26layer=GruverOversikt', 
#    'GruverOversikt').add_to(m)








    #--



#    add = '/MapServer/tile/{z}/{y}/{x}'
#    ESRI = dict(World_Ocean_Base='http://services.arcgisonline.com/arcgis/rest/services/Ocean/World_Ocean_Base',
#                World_Navigation_Charts='http://services.arcgisonline.com/ArcGIS/rest/services/Specialty/World_Navigation_Charts',
#                World_Ocean_Reference='http://services.arcgisonline.com/arcgis/rest/services/Ocean/World_Ocean_Reference',
#                NatGeo_World_Map='http://services.arcgisonline.com/arcgis/rest/services/NatGeo_World_Map/MapServer',
#                World_Imagery='http://services.arcgisonline.com/arcgis/rest/services/World_Imagery/MapServer',
#                World_Physical_Map='http://services.arcgisonline.com/arcgis/rest/services/World_Physical_Map/MapServer',
#                World_Shaded_Relief='http://services.arcgisonline.com/arcgis/rest/services/World_Shaded_Relief/MapServer',
#                World_Street_Map='http://services.arcgisonline.com/arcgis/rest/services/World_Street_Map/MapServer',
#                World_Terrain_Base='http://services.arcgisonline.com/arcgis/rest/services/World_Terrain_Base/MapServer',
#                World_Topo_Map='http://services.arcgisonline.com/arcgis/rest/services/World_Topo_Map/MapServer')

#    for tile_name, tile_url in ESRI.items():
#        tile_url += add
#        #folium.TileLayer(tile_url,attr=tile_name).add_to(m)

#    st.write('æ')

    #folium.WmsTileLayer(', 'gruver')

    #folium.WmsTileLayer('https://geo.ngu.no/mapserver/LosmasserWMS2', 'Losmasse flate').add_to(m)


#    url= "http://mesonet.agron.iastate.edu/cgi-bin/wms/nexrad/n0r.cgi"
#    layers= ['nexrad-n0r-900913']
#    folium.WmsTileLayer(url, 
#    layers, 
#    fmt='image/png', 
#    transparent=False, 
#    attr='Løsmasser',
#    name='Løsmasser').add_to(m)


#    tooltip = "Liberty Bell"
#    folium.Marker(
#        [59.949610, 5.150282], popup="Liberty Bell", tooltip=tooltip
#    ).add_to(m)


#    inline_map(m)
#    folium_static(m)


