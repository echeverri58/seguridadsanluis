import pandas as pd
import matplotlib.pyplot as plt

def grafica_hurto_vehiculos():
    # URL de la base de datos CSV
    url = "https://www.datos.gov.co/resource/csb4-y6v2.csv?$query=SELECT%0A%20%20%60fecha_hecho%60%2C%0A%20%20%60cod_depto%60%2C%0A%20%20%60departamento%60%2C%0A%20%20%60cod_muni%60%2C%0A%20%20%60municipio%60%2C%0A%20%20%60tipo_delito%60%2C%0A%20%20%60zona%60%2C%0A%20%20%60cantidad%60%0AWHERE%0A%20%20caseless_one_of(%60departamento%60%2C%20%22ANTIOQUIA%22)%0A%20%20AND%20caseless_one_of(%60municipio%60%2C%20%22SAN%20LUIS%22)%0AORDER%20BY%20%60fecha_hecho%60%20DESC%20NULL%20LAST"

    # Carga el archivo CSV directamente desde la URL en un DataFrame
    df = pd.read_csv(url)

    # Convierte la columna 'fecha_hecho' a datetime
    df['fecha_hecho'] = pd.to_datetime(df['fecha_hecho'])

    # Obtiene la fecha del hecho para cada registro
    df['fecha_hecho'] = df['fecha_hecho'].dt.year

    # Agrupa los datos por año y suma la cantidad de hechos por cada año
    cantidad_por_año = df['cantidad'].groupby(df['fecha_hecho']).sum()

    # Convierte los valores de la lista cantidad_por_año a enteros
    cantidad_por_año = cantidad_por_año.astype('int')

    # Convierte los valores de la columna 'fecha_hecho' a string
    cantidad_por_año.index = cantidad_por_año.index.astype('str')

    # Crea la gráfica de barras
    plt.bar(cantidad_por_año.index, cantidad_por_año.values)
    plt.xlabel('Año')
    plt.ylabel('Cantidad')
    plt.title('Hurto a vehículos en San Luis Antioquia por año')

    # Agrega el texto a la barra
    for i in range(len(cantidad_por_año)):
        plt.annotate(cantidad_por_año.values[i], (cantidad_por_año.index[i], cantidad_por_año.values[i]), ha='center', va='bottom')

    # Establece los valores de los ejes 'x'
    plt.xticks(cantidad_por_año.index, rotation=90)

    # Muestra la gráfica
    plt.show()

# Llamada a la función principal cuando se ejecuta el script directamente
if __name__ == "__main__":
    grafica_hurto_vehiculos()

