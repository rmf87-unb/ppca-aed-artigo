from helpers import (
    hungaro,
)

url = "./dados_320_3000.csv"
id_rotulo = "IDENTIFICADOR"
allocation = "CARGO"
param_a = "PERCENT_PRI"
param_b = "DISTANCE_KM"
peso_a = 0.5

custo_total, filename = hungaro(url, id_rotulo, param_a, param_b, peso_a, allocation)
print(
    f"Resultado da alocação pelo Método Húngaro com custo total de {custo_total} salvo no arquivo {filename}"
)
