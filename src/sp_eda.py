# Tratamiento de datos
import pandas as pd



def eda_preliminar (df):

    """
    Realiza un análisis exploratorio preliminar sobre un DataFrame dado.

    Este análisis incluye:
    - Muestra aleatoria de 5 filas del DataFrame.
    - Información general del DataFrame (tipo de datos, nulos, etc.).
    - Porcentaje de valores nulos por columna.
    - Conteo de filas duplicadas.
    - Distribución de valores para columnas categóricas.

    Parameters:
    df (pd.DataFrame): DataFrame a analizar.

    Returns:
    None
    """


    display(df.sample(5))

    print('-----------------')

    print('DIMENSIONES')

    print(f'Nuestro conjunto de datos presenta un total de {df.shape[0]} filas y {df.shape[1]} columnas')

    print('-----------------')

    print('INFO')

    display(df.info())  

    print('-----------------')
    print('NULOS')

    display(df.isnull().mean()*100)

    print('-----------------')
    print('DUPLICADOS')

    print(f'Tenemos un total de {df.duplicated().sum()} duplicados')

    print('-----------------')
    print('FRECUENCIA CATEGÓRICAS')
    for col in df.select_dtypes(include= 'object').columns:
        print(col.upper())
        print(df[col].value_counts())
        print('-------')

    print('-----------------')
    print('ESTADÍSTICOS NUMÉRICAS')
    display(df.describe().T)