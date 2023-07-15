import os

def run_crime():

    # Import modules
    print('Importing modules...')
    from modules.ingest import ingest_excel
    from modules.transform import transform, convert_geodataframe
    from modules.folium_plot import plot_map

    # Setting directories
    print('Setting directories...')
    current_directory = os.getcwd()
    parent_directory = os.path.dirname(current_directory)
    data_directory = os.path.join(parent_directory, "data")
    html_export_directory = parent_directory

    # Ingest
    print('Ingesting data...')
    df = ingest_excel(data_directory+'\SPDadosCriminais_2023.xlsx')

    # Transform
    print('Transforming data...')
    df = transform(df,5)
    df = convert_geodataframe(df,'LONGITUDE','LATITUDE')

    # Plot
    print('Exporting map...')
    m = plot_map(df,[-23.58, -46.64],html_export_directory)

    return df

run_crime()