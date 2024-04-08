import pandas as pd
from funciones import leer_datos, medias


path ='../data/datos_examen.csv'
def main():
    df=leer_datos(path)
    medias(df)
    
    
if __name__ =='__main__':
    main()
