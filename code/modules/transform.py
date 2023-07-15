import pandas as pd
import geopandas as gpd

def transform(df,mes_2023):

    # Adicionar info do Dia    
    df['DIA'] = df['DATA_OCORRENCIA_BO'].dt.strftime('%a')

    # Adicionar infos de Data & Hora mais curtas
    df['DATA_CURTA'] = df['DATA_OCORRENCIA_BO'].dt.strftime('%d/%m')
    df['HORA_CURTA'] = pd.to_datetime(df['HORA_OCORRENCIA_BO'],format='%H:%M:%S').dt.strftime('%H:%M')
    
    # Filtros

    # Cidade
    df = df[df['CIDADE'] == 'S.PAULO']
    
    # Dados Georeferenciados
    df = df[(df['LONGITUDE']!=0)]
    df = df[~df['LONGITUDE'].isna()]

    # Mes
    df = df[(df['MÊS_ESTÁTISTICA'].isin(mes_2023))]
    
    return df

def convert_geodataframe(df,long,lat):

    # Converter DataFrame p/ GeoDataFrame
    geometry = gpd.points_from_xy(df[long], df[lat])
    
    df_converted = gpd.GeoDataFrame(df, geometry=geometry)
    df_converted = df_converted.reset_index(drop=True)

    return df_converted

