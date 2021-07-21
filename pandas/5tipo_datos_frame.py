import pandas as pd

import numpy as np

dir_pandas = "./db/{}".format("Meteorite_Landings.csv")

df_meteorites = pd.read_csv(dir_pandas)

#redondear los decimales en el describe

pd.options.display.float_format = "{:,f}".format

#print(df_meteorites)

#con .head podemos ver las primeras x filas  al inicio ejemplo 20 lineas

print(df_meteorites.head(20))

#con .tail podemos ver las ultimas x filas al dinas ejemplo 10 lineas

print(df_meteorites.tail(10))

#mostrar una muestra aleatoria de x filas

print(df_meteorites.sample(10))

#mostrar el numero de filas y columnas de nuestro fram

print("Es un dataframe de filas x columnas")

print(df_meteorites.shape)

#el tamaño de nuestro dataframe = filas x columnas

print("tamaño de nuestro Frame")

print(df_meteorites.size)

#describe cualidades estadisticas de mi base de datos

print(df_meteorites.describe())

#describe con mas atos de las variables texto

print(df_meteorites.describe(include="all"))

#poara ver las categorias de las variables

print(df_meteorites.info())

#o solo el tipo de las variables

print(df_meteorites.dtypes)

#cambiar por los mejores formatos de nuestro frame

print(df_meteorites.convert_dtypes().dtypes)