import pandas as pd
def leer_datos(path):
    '''Se utiliza esta funcion para poder realizar la lectura de datos a partir de una direccion proporcionada
    Luego corrige el tipo de la variable TS'''
    df = pd.read_csv(path)
    df['TS']=pd.to_datetime(df['TS'])
    return df


def medias(df)->str:
    '''A partir del data frame que se realizo antes, se crea una lista de elementos unicos y se tranforma en una lista
    luego se realiza un filtro por cada elemento de la lista y se imprime el promedio de cada alumno'''
    lista= df['Tag'].unique().tolist()
    for i in lista:
        data_filter = df[df['Tag'] == i]
        med=(data_filter['Value'].mean())
        print(f'La media de {i} es {med}')