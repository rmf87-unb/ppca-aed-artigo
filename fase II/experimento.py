import pandas as pd
from scipy.optimize import linear_sum_assignment
from sklearn import preprocessing

from helpers import (
    add_scaled_index,
    calculate_cost,
    data_load_preprocessing,
    rotate_and_fill,
    save_txt,
)

# carga dos dados e conversão pra int
# url = "dados_algoritmo2.txt"
url = "./dados_50_50.csv"
allocation = "CARGO"
param_a = "PERCENT_PRI"
param_b = "DISTANCE"
peso_a = 0.5


dados = data_load_preprocessing(url)
dados = add_scaled_index(dados, param_a, param_b, peso_a)
print(dados.head())
dados = rotate_and_fill(dados, allocation)
print(dados.head())

custo_total, matriz_custo, lin, col = calculate_cost(dados)

filename = save_txt(lin, col, matriz_custo, dados, custo_total, allocation)

for i, j in zip(lin, col):
    print(
        f"Militar {dados.index[i]} no cargo {dados.columns[j]} com custo {matriz_custo[i,j]}"
    )

print(f"custo total {custo_total}")
