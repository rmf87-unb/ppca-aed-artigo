from types import NoneType
import pandas as pd


def export_a_partition(df: pd.DataFrame, id_rotulo, id_limit, param_a, a_limit):
    try:
        # check
        rot_a = df.get(id_rotulo)
        if isinstance(rot_a, NoneType):
            raise KeyError(id_rotulo)
        rot_b = df.get(param_a)
        if isinstance(rot_b, NoneType):
            raise KeyError(param_a)

        # partition data
        partition = df.query(f"{id_rotulo} <= {id_limit}")
        nth_a = (
            partition.sort_values(param_a)
            .drop_duplicates(param_a)[param_a]
            .iloc[a_limit - 1]
        )
        query = f"{param_a} <= {nth_a}"
        partition = partition.query(query)

        partition = partition.sort_values([id_rotulo, param_a])
        partition.to_csv(
            path_or_buf=f"./dados_{id_limit}_{a_limit}.csv",
            index=False,
            sep=";",
            decimal=",",
        )
    except KeyError as err:
        print("Coluna não existe nos dados: ", err)
        exit(1)
