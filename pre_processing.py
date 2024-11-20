import pandas as pd
import numpy as np


# carga dos dados e conversão pra int
url = "dados_algoritmo2.txt"
dados = pd.read_csv(url, delimiter=";", encoding="ascii", decimal=",")
# unique = pd.unique(dados["CARGO"])
# unique = np.sort(unique)
# print(unique[:50])

dados_50_cargos = dados.query("CARGO <= 74")
# print(dados_50_cargos.groupby("IDENTIFICADOR").count())
dados_50_50 = dados_50_cargos.query("IDENTIFICADOR <= 50")
# print(dados_50_50[:150])

dados_50_50.to_csv(path_or_buf="./dados_50_50.csv", index=False, sep=";", decimal=",")

# dados_1_cargos = dados.query("IDENTIFICADOR == 2")
# print(dados_1_cargos)
# dados_1_cargos.sort_values("CARGO", inplace=True)

# print(dados_1_cargos.sort_values("CARGO").count())
# dados_1_cargos = dados.query("IDENTIFICADOR == 1")
# print(dados_50_50.groupby("IDENTIFICADOR").count())
# print(dados.groupby("IDENTIFICADOR").count())
# dados_50_50.group("MILITAR").count()
# print(dados_50_50.head(50))
