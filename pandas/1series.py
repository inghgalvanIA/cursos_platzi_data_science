import pandas as pd
from pandas.core.indexes.base import Index

import numpy as np

#crear una serie por medio de una lista
serie = pd.Series([10,9,8,7,6])

print(serie)

#valores 

print("valores de la lista")

valores = serie.values

print(valores)

#informacion del indice

print("informacion de los indices")

indices = serie.index

print(indices)

#conocer el numero de elementos

print("conocer el numero de elementos de la serie")

print(serie.shape)

#llamar un elemento de un cierto indice

print("imprimiendo un valor por medio de su indice ej. 4")

print(serie[4])

#imprimir varios elementos de la serie 

print("imprimiendo varios indices ej: 0,4,2")

print(serie[[0,4,2]])

#cambiar indice

print("cambiar los indices ")

sr1 = pd.Series([10,9,8,7,6], index = ["a","b","c","d","e" ])

print(sr1)

#creando series a apartir de llaves

llave = {"CO":100,"MX":200 ,"AR":200}

print("creando una serie a partir de una llave")

llave_serie = pd.Series(llave)

print(llave_serie)

#objeto nan (objeto nulo)

nulo = np.nan

print(nulo)

#valores  nulos si = True no = false
si_nulos = llave_serie.isnull()

no_nulos = llave_serie.notnull()

