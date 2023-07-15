import pandas as pd

def ingest_excel(file_path):
    
    df = pd.read_excel(file_path,engine='openpyxl')

    return df
