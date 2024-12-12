from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpBinary
import pandas as pd

# Carregar os dados do arquivo CSV
data = pd.read_csv("dados_50_50.csv", sep=";", decimal=",")

# Criar o problema de otimização
problem = LpProblem("Alocacao_Funcionarios", LpMinimize)

# Criar variáveis de decisão
# x[i, j] = 1 se o funcionário i for alocado ao cargo j, caso contrário 0
x = LpVariable.dicts(
    "x", ((row.IDENTIFICADOR, row.CARGO) for _, row in data.iterrows()), cat=LpBinary
)

# Definir pesos para a função objetivo
peso_percent_pri = 0.5
peso_distance_km = 0.5

# Função objetivo: minimizar a soma ponderada de PERCENT_PRI e DISTANCE_KM
problem += lpSum(
    (peso_percent_pri * row.PERCENT_PRI + peso_distance_km * row.DISTANCE_KM)
    * x[row.IDENTIFICADOR, row.CARGO]
    for _, row in data.iterrows()
)

# Restrições
# Cada funcionário deve ser alocado a exatamente um cargo
for identificador in data.IDENTIFICADOR.unique():
    problem += (
        lpSum(
            x[identificador, cargo]
            for cargo in data[data.IDENTIFICADOR == identificador].CARGO
        )
        == 1
    )

# Cada cargo deve ser ocupado por no máximo um funcionário
for cargo in data.CARGO.unique():
    problem += (
        lpSum(
            x[identificador, cargo]
            for identificador in data[data.CARGO == cargo].IDENTIFICADOR
        )
        <= 1
    )

# Resolver o problema
problem.solve()

# Extrair e imprimir as alocações
allocations = [
    (identificador, cargo)
    for identificador, cargo in x
    if x[identificador, cargo].varValue == 1
]
print("Alocações ótimas:")
for identificador, cargo in allocations:
    print(f"Funcionário {identificador} alocado ao cargo {cargo}")
