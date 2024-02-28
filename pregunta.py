"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd

pd.options.display.max_columns = None
pd.options.display.max_rows = None

def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0)

    columnas_str = [df[col].name if df[col].dtype == 'object' else '' for col in df.columns]
    columnas_str= [item for item in columnas_str if item.strip()]
    df = df.replace('-', ' ', regex=True).replace('_',' ', regex=True)

    for col in columnas_str:
        df[col] = df[col].str.lower().str.strip()

    df['comuna_ciudadano'] = df['comuna_ciudadano'].astype(int)
    df['estrato_ciudadano'] = df['estrato'].astype(int)
    df['monto_del_credito'] = df['monto_del_credito'].str.strip(' ').str.replace('[ ,$]', '', regex=True).str.replace('\.00','',regex=True).astype(float)
    df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'], format='%d/%m/%Y', errors='coerce').fillna(pd.to_datetime(df['fecha_de_beneficio'], format='%Y/%m/%d', errors='coerce'))
    replacement_dict = {'bel¿n': 'belén', 'antonio nari¿o': 'antonio nariño'}
    df['barrio'] = df['barrio'].replace(replacement_dict)
    df = df.dropna()
    df = df.drop_duplicates()

    return df
print(clean_data().barrio.value_counts())