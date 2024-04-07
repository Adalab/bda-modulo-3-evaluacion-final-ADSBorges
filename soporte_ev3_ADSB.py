
import matplotlib.pyplot as plt


def plot_histogram(df, columna, bins=20):
    """
    Función para graficar un histograma de una columna de un DataFrame.
    Parámetros:
        - df: nombre del DataFrame
        - columna: nombre de la columna del DataFrame que se utilizará para el histograma
        - bins: número de contenedores para el histograma
    """
    plt.hist(df[columna], bins=bins)
    plt.title(f'Histograma de la columna "{columna}"')
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')
    plt.show()

# Sintaxis de uso:
# plot_histogram(df, 'columna')



def plot_dispersion(df, columna1, columna2):
    """
   Función para obtener un gráfico de dispersión para comparar dos columnas de un DataFrame.

    Parámetros:
    - df : DataFrame
        El DataFrame que contiene los datos.
    - columna1 : str
        El nombre de la primera columna a comparar.
    - columna2 : str
        El nombre de la segunda columna a comparar.
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(df[columna1], df[columna2])
    plt.title(f'Relación entre {columna1} y {columna2}')
    plt.xlabel(columna1)
    plt.ylabel(columna2)
    plt.grid(True)
    plt.show()

# Puede llamar a la función así:
# plot_dispersion(df, 'columna1', 'columna2')




def exploracion_datos(df):
    """
    Realiza una exploración básica de los datos en un DataFrame.
    Imprime información sobre la forma del DataFrame, la cantidad de valores nulos por columna,
    la cantidad de duplicados en el DataFrame y los tipos de datos de cada columna.

    Parámetros:
    - df : el DataFrame que se desea explorar.
    Retorna:
    - Imprime información sobre los datos en la salida estándar.
    
    """
    
    forma = df.shape
    print(f"La forma es {forma}")
    print("---------------")
    nulos = df.isna().sum()
    print(f"Los nulos son:")
    display(nulos)
    print("---------------")
    duplicados = df.duplicated().sum()
    print(f"Hay {duplicados} duplicados")
    print("---------------")
    tipo_dato = df.dtypes
    print(f"Los datos son de tipo:")
    display(tipo_dato)
    print("---------------")
    columnas = df.columns
    print(f"Las columnas son {columnas}")

# Se puede llamar a la función así:
# exploracion_datos(df)