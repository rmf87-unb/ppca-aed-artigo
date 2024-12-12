import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpBinary

# Carregar os dados
data = pd.read_csv("dados_50_50.csv", sep=";")

# Normalizar PERCENT_PRI e DISTANCE_KM
scaler = MinMaxScaler()
data[["PERCENT_PRI", "DISTANCE_KM"]] = scaler.fit_transform(
    data[["PERCENT_PRI", "DISTANCE_KM"]]
)

# Criar o problema de otimização
problem = LpProblem("Alocacao_Funcionarios", LpMinimize)

# Criar variáveis de decisão
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
for identificador in data.IDENTIFICADOR.unique():
    problem += (
        lpSum(
            x[identificador, cargo]
            for cargo in data[data.IDENTIFICADOR == identificador].CARGO
        )
        == 1
    )

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
