import pandas as pd

import numpy as np

dir_pandas = "./db/{}".format("Meteorite_Landings.csv")

df_meteorites = pd.read_csv(dir_pandas)

#redondear los decimales en el describe

pd.options.display.float_format = "{:,f}".format

print(df_meteorites)

#copiar un dataframe poniendo que la copia es profunda

df_copia = df_meteorites.copy(deep=True)

print(df_copia)