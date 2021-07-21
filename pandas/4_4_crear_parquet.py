import pandas as pd

import numpy as np

dir_pandas = "./db/{}".format("test.parquet")


dict_data = {
    'edad': [10,9,13,14,12,11,12],
    'cm': [115,110,130,155,125,120,125],
    'pais':['co','mx','co','mx','mx','ch','ch'],
    'genero':['M','F','F','M','M','M','F'],
    'Q1':[5,10,8,np.nan,7,8,3],
    'Q2':[7,9,9,8,8,8,9]
}

#pasando el diccionario a dataframe

df = pd.DataFrame(dict_data)

print(df)

#creando el archivo en json

df.to_parquet(dir_pandas)

leer = pd.read_parquet(dir_pandas)

print(leer)