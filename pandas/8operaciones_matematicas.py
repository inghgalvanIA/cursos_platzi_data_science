import pandas as pd

import numpy as np

dir_pandas = "./db/{}".format("london_merged.csv")

df_bicicletas = pd.read_csv(dir_pandas)

print(df_bicicletas)

print(df_bicicletas.dtypes)

#cambiar el formato de objeto a fecha

df_bicicletas["timestamp"] = pd.to_datetime(df_bicicletas["timestamp"])

print(df_bicicletas)

print(df_bicicletas.dtypes)

#quitaremos la primera columna 

df_bicicletas = df_bicicletas.iloc[:,1:]

print(df_bicicletas)

df = np.sin(df_bicicletas["wind_speed"]**2)+10
print(df)