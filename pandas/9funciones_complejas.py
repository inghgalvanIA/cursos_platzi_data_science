import pandas as pd

import numpy as np

dir_pandas = "./db/{}".format("london_merged.csv")

df_bicicletas = pd.read_csv(dir_pandas)

print(df_bicicletas)

#una funcion

def fun_1(x):

    y = x**2+1

    return y

print(fun_1(10))

#aplciar un rango de datos

print(fun_1(np.arange(-5,6)))

#para aplicar una funcion en un dataframe

print(df_bicicletas["t1"].apply(fun_1))

#funcion lambda

print("trabnsformacion de c a k")

print(df_bicicletas["t1"].apply(lambda x:x+273))

#calcular el promedio de cada columna

#print(df_bicicletas.apply(lambda x: x.mean()))

#print(df_bicicletas.apply(lambda x: x.mean(),axis=1))

#desviacion estandar

#print(df_bicicletas.apply(lambda x: x.std(),axis=1))

#aplicar a todo el dataframe

print(df_bicicletas.applymap(lambda x: x/1000))