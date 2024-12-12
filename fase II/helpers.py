from types import NoneType
import pandas as pd
from sklearn import preprocessing
from scipy.optimize import linear_sum_assignment
import csv
from datetime import datetime


def data_load_preprocessing(url):
    try:
        df = pd.read_csv(url, delimiter=";", encoding="ascii", decimal=",")
        return df
    except OSError as err:
        print("Arquivo não encontrado:", err.filename)
        exit(1)


def add_scaled_index(df: pd.DataFrame, param_a, param_b, peso_a):
    try:
        # check
        rot_a = df.get(param_a)
        if isinstance(rot_a, NoneType):
            raise KeyError(param_a)
        rot_b = df.get(param_b)
        if isinstance(rot_b, NoneType):
            raise KeyError(param_b)

        # transform
        scaler = preprocessing.MinMaxScaler()
        param_a_s = param_a + "_s"
        param_b_s = param_b + "_s"
        df[[param_a_s]] = scaler.fit_transform(df[[param_a]])
        df[[param_b_s]] = scaler.fit_transform(df[[param_b]])
        df["custo"] = df[param_a_s] * peso_a + df[param_b_s] * (1 - peso_a)
        return df
    except KeyError as err:
        print("Coluna não existe nos dados: ", err)
        exit(1)


def rotate_and_fill(df: pd.DataFrame, objetivo: str):
    try:
        # check
        # rot_id = df.get("ID")
        # if isinstance(rot_id, NoneType):
        #     raise KeyError("ID")

        # rotate
        df_r = df.pivot_table(
            values="custo", index="ID", columns=objetivo, aggfunc="max"
        ).fillna(1)
        return df_r
    except KeyError as err:
        print("Coluna não existe nos dados: ", err)
        exit(1)


def calculate_cost(df: pd.DataFrame):
    cost_matrix = df.to_numpy()
    lin, col = linear_sum_assignment(cost_matrix)
    total_cost = cost_matrix[lin, col].sum()
    return total_cost, cost_matrix, lin, col


def save_txt(lin, col, matriz_custo, df, custo_total, allocation):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"alocacao_hungaro_{timestamp}.txt"
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", allocation, "Custo"])
        for i, j in zip(lin, col):
            writer.writerow([df.index[i], df.columns[j], matriz_custo[i, j]])
        writer.writerow([])
        writer.writerow(["Custo Total", custo_total, ""])
    return filename


# Created/Modified files during execution:
# assignment_report_YYYYMMDD_HHMMSS.csv will be created when function is run
