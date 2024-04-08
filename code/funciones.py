import pandas as pd
def leer_datos(path):
    df = pd.read_csv(path)
    df['TS']=pd.to_datetime(df['TS'])
    medias(df)

def medias(df:str)->str:
    lista= df['Tag'].unique().tolist()
    for i in lista:
        data_filter = df[df['Tag'] == i]
        med=(data_filter['Value'].mean())
        print(f'La media de {i} es {med}')