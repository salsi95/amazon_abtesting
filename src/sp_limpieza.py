import pandas as pd

def minus (df):
    """
    Convierte a minúsculas los valores de todas las columnas categóricas de un DataFrame.

    Recorre cada columna de tipo objeto en el DataFrame y convierte sus valores a minúsculas, 
    facilitando el análisis de datos sin distinción de mayúsculas y minúsculas.

    Parameters:
    df (pd.DataFrame): DataFrame en el cual se procesarán las columnas categóricas.

    Returns:
    None
    """

    for col in df.select_dtypes(include = 'O').columns:
        df[col] = df[col].str.lower()


def comas (df):

    """
    Reemplaza comas con puntos en columnas específicas de un DataFrame.

    Para cada columna en la lista proporcionada, convierte las comas (',') a puntos ('.'), 
    facilitando el análisis de datos numéricos en sistemas que utilizan el punto como separador decimal.

    Parameters:
    df (pd.DataFrame): DataFrame que contiene las columnas a procesar.
    lista_col (list of str): Lista con los nombres de las columnas en las que se deben reemplazar comas por puntos.

    Returns:
    None
    """

    for col in df.select_dtypes(include ='O'):
        df[col] = df[col].str.replace(',','.')
        try:
            df[col] = df[col].astype('float64')
        except:
            pass

def espacios (df):
    """
    Reemplaza espacios con guiones bajos en los valores de todas las columnas de tipo texto en un DataFrame.

    Para cada columna del DataFrame, intenta reemplazar los espacios en blanco (' ') 
    con guiones bajos ('_') en los valores de texto, facilitando el manejo de datos sin espacios.

    Parameters:
    df (pd.DataFrame): DataFrame en el cual se procesarán las columnas de tipo texto.

    Returns:
    None
    """

    for col in df.select_dtypes(include = 'O').columns:
        df[col] = df[col].str.replace(' ', '_')