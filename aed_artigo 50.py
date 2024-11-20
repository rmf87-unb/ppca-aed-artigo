import numpy as np
import pandas as pd
from scipy.optimize import linear_sum_assignment
from sklearn import preprocessing

# carga dos dados e conversão pra int
url = "./dados_50_50.csv"
dados = pd.read_csv(url, delimiter=";", encoding="ascii", decimal=",")

# normalizando as variáveis que serão utilizadas para gerar o indice que queremos minimizar
# Como a variável PERCENT_PRI já é alguma coisa variando de 0 a 1,
# a ideia é modificar apenas o DISTANCE_KM para que também varie de 0 a 1
# normalização da distância
scaler = preprocessing.MinMaxScaler()
dados[["DISTANCE_KM_R"]] = scaler.fit_transform(dados[["DISTANCE_KM"]])
# print(len(pd.unique(dados["CARGO"])))

# índice geral que vamos minimizar.
# 1 - dando um peso maior para a distância, pois quanto menor a distância mais barata é a movimentacao
# dados["INDICE_100DS"] = dados["DISTANCE_KM_R"] * 1 + dados["PERCENT_PRI"] * 0
# dados["INDICE_20D80S"] = dados["DISTANCE_KM_R"] * 0.2 + dados["PERCENT_PRI"] * 0.8
# dados["INDICE_80D20S"] = dados["DISTANCE_KM_R"] * 0.8 + dados["PERCENT_PRI"] * 0.2
dados["INDICE_50D50S"] = dados["DISTANCE_KM_R"] * 0.5 + dados["PERCENT_PRI"] * 0.5
# dados["INDICE_0D100S"] = dados["DISTANCE_KM_R"] * 0.0 + dados["PERCENT_PRI"] * 1
print(dados.head())

# dados2 = dados[["IDENTIFICADOR", "CARGO", "INDICE_50D50S"]]
# tratamento dos dados faltantes
pivoted_data = dados.pivot_table(
    values="INDICE_50D50S", index="IDENTIFICADOR", columns="CARGO", aggfunc="max"
).fillna(1)

print(pivoted_data.head())


cost_matrix = pivoted_data.to_numpy()

# função de otimização
lin, col = linear_sum_assignment(cost_matrix)


total_cost = cost_matrix[lin, col].sum()

for i, j in zip(lin, col):
    print(
        f"Militar {pivoted_data.index[i]} no cargo {pivoted_data.columns[j]} com custo {cost_matrix[i,j]}"
    )

print(f"custo total {total_cost}")
