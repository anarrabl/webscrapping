import pandas as pd
import matplotlib.pyplot as plt

# Paso 1: Abrir el archivo CSV con pandas
archivo = '../data/noticias.csv'
datos = pd.read_csv(archivo)
#(archivo, encoding='utf-8'
# Paso 2: Visualizar los primeros registros para entender la estructura de los datos
print(datos.head())

# Paso 3: Crear un gráfico con Matplotlib
plt.scatter(datos['categoria'], datos['fecha'])
plt.title('Gráfico de dispersión de categorias vs fechas')
plt.xlabel('categoria')
plt.ylabel('fecha')

# Mostrar el gráfico en la consola de Pycharm:
plt.show()