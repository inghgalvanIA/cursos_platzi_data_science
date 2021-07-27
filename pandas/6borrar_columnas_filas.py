import pandas as pd

import numpy as np

dir_pandas = "./db/{}".format("Meteorite_Landings.csv")

df_meteorites = pd.read_csv(dir_pandas)

#redondear los decimales en el describe

pd.options.display.float_format = "{:,f}".format

print(df_meteorites)

#borar una columna axis = 1
#borrar una fila axis = 0

df_meteorites.drop(["reclat"],axis=1,inplace=True)

print(df_meteorites)

#para borrar los indices en filas

print(df_meteorites.drop([0,2,4,6]))

#df_meteorites.drop(columns=["id","recclass"],index=[0,2,4,6])