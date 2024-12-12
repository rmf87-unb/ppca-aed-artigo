from helpers import (
    hungaro,
)

url = "./dados_50_50.csv"
allocation = "CARGO"
param_a = "PERCENT_PRI"
param_b = "DISTANCE"
peso_a = 0.5

custo_total, filename = hungaro(url, param_a, param_b, peso_a, allocation)
print(
    f"Resultado da alocação pelo Método Húngaro com custo total de {custo_total} salvo no arquivo {filename}"
)
