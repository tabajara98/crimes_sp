import folium
from folium.plugins import MarkerCluster
from folium.plugins import HeatMap

# Map
def plot_map(df,start_coord,export_path):

    # Instanciando o mapa do folium nas coordenadas iniciais
    m = folium.Map(location=start_coord, tiles=None, zoom_start=14)
    folium.raster_layers.TileLayer(tiles='openstreetmap', name='Crimes').add_to(m)

    # Criar listas dos dados de coordenadas
    geo_df_list = [(point.xy[1][0], point.xy[0][0]) for point in df.geometry]

    heatmap_group = folium.FeatureGroup(name='Mapa de Calor',show=False)
    HeatMap(geo_df_list,min_opacity=0.3,max_opacity=0.83,use_local_extrema=False).add_to(heatmap_group.add_to(m))
    
    # Definindo clusters
    marker_group = folium.FeatureGroup(name='Clusters')
    marker_cluster = MarkerCluster().add_to(marker_group)

    # Iterar pela lista adicionando marcadores
    i = 0
    for coordinates in geo_df_list:

        # Place the markers with the popup labels and data
        folium.Marker(
            location=coordinates,
            popup=folium.Popup("<b>Natureza:</b> "+ str(df.NATUREZA_APURADA[i])+
            '<br><b>Conduta:</b> ' + str(df.DESCR_CONDUTA[i])+
            '<br><b>Data e Hora:</b> ' + str(df.DATA_CURTA[i]) + ' ' + str(df.HORA_CURTA[i])+
            '<br><b>Dia:</b> ' + str(df.DIA[i]), max_width=2000),
            icon=folium.Icon(color="gray", icon="info-sign"),
        ).add_to(marker_cluster)

        i = i + 1

    # Add the FeatureGroup to the map
    marker_group.add_to(m)

    folium.LayerControl(collapsed=False,).add_to(m)

    m.save(export_path+'\crimes_sp_map.html')