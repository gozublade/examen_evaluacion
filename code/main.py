import pandas as pd
from funciones import leer_datos, medias


path ='../data/datos_examen.csv'
alumno='Manuel'
def main():
    df=leer_datos(path)
    medias(df,alumno)
    
    
if __name__ =='__main__':
    main()
