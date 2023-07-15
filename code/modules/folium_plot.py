import folium
from folium.plugins import MarkerCluster

# Map
def plot_map(df,start_coord,export_path):

    # Instanciando o mapa do folium nas coordenadas iniciais
    m = folium.Map(location=start_coord, tiles="OpenStreetMap", zoom_start=13)

    # Definindo clusters
    marker_cluster = MarkerCluster().add_to(m)

    # Criar listas dos dados de coordenadas
    geo_df_list = [[point.xy[1][0], point.xy[0][0]] for point in df.geometry]

    # Iterar pela lista adicionando marcadores
    i = 0
    for coordinates in geo_df_list:

        # Place the markers with the popup labels and data
        folium.Marker(
            location=coordinates,
            popup=folium.Popup("Natureza: "+ str(df.NATUREZA_APURADA[i])+
            '<br> Conduta: ' + str(df.DESCR_CONDUTA[i])+
            '<br> Data e Hora: ' + str(df.DATA_CURTA[i]) + ' ' + str(df.HORA_CURTA[i])+
            '<br> Dia: ' + str(df.DIA[i]), max_width=2000),
            icon=folium.Icon(color="gray", icon="info-sign"),
        ).add_to(marker_cluster)

        i = i + 1

    m.save(export_path+'\crimes_sp_map.html')