"""
dataframe es una estructura bidimencional
las columans tienen diferentes tipos de datos

"""

import pandas as pd

import numpy as np

#version de pandas

print("version de pandas ocupada")

print(pd.__version__)

dict = {"CO":[100,800,200],"MX":[100,200,300],"CH":[300,500,400]}

print(dict)

print("convertir nuestro diccionaria a serie")

serie = pd.Series(dict)

print(serie)

print("convertir deun diccionario a un dataframe")

data_f = pd.DataFrame(dict)

print(data_f)

dict_data_dos = {
    'edad': [10,9,13,14,12,11,12],
    'cm': [115,110,130,155,125,120,125],
    'pais':['co','mx','co','mx','mx','ch','ch'],
    'genero':['M','F','F','M','M','M','F'],
    'Q1':[5,10,8,np.nan,7,8,3],
    'Q2':[7,9,9,8,8,8,9]
}

print("dataframe 2")

data_f_dos = pd.DataFrame(dict_data_dos)

print(data_f_dos)

print("cambiando los indices")

data_f_dos = pd.DataFrame(dict_data_dos, index=["Ana","Carlos","Eduardo","Rosa","Luz","Roberto","Ismael"])

print(data_f_dos)

print("ver configuracion de nuestro indice")

print(data_f_dos.index)

print("ver las columnas de nuestro dataframe")

print(data_f_dos.columns)

print("ver los valores de nuestro dataframe")

print(data_f_dos.values)

print("selecciona un conjunto de valores ejemplo columna edad")

print(data_f_dos["edad"])

print("selecciona varias columnas ejemplo edad, cm, Q1 ")

print(data_f_dos[["edad","cm","Q1"]])

print("para selecionar una fila en especifico ejemplo ana en edad,cm,Q1")

print(data_f_dos.loc["Ana",["edad","cm","Q1"]])

print("para selecionar  filas en especifico ejemplo ana en edad,cm,Q1")

print(data_f_dos.loc[["Ana","Carlos"],["edad","cm","Q1"]])

print("seelcionar un valor por medio de indice ejemplo Eduardo cm")

#iloc[filas,columnas]

print(data_f_dos.iloc[2,1])

#otro ejemplo

print(data_f_dos.iloc[2,[1,3]])

#columna entera se ocupan :

print(data_f_dos.iloc[:,[1,3]])

#filtro basado en condiciones 

print("filtran los estudiantes mayores de 12 años")

print(data_f_dos[data_f_dos["edad"]>=12])

print("filtrar a los mayores de 12 años y pais MX")

print(data_f_dos[(data_f_dos["edad"] >=12) & (data_f_dos["pais"] == "mx")])

#otra formato de basado en condiciones

print(data_f_dos.query("edad > 12"))

#comparando 2 columnas

print(data_f_dos[data_f_dos["Q2"] >= data_f_dos["Q1"]])