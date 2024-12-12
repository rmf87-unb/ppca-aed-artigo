from helpers import data_load_preprocessing
from pre_processing_helpers import export_a_partition
import pandas as pd


url = "dados_algoritmo2.txt"
id_rotulo = "IDENTIFICADOR"
param_a = "CARGO"
a_limit = 50
id_limit = 50

dados = data_load_preprocessing(
    url,
)
export_a_partition(dados, id_rotulo, 50, param_a, 50)
export_a_partition(dados, id_rotulo, 50, param_a, 200)
export_a_partition(dados, id_rotulo, 100, param_a, 100)
export_a_partition(dados, id_rotulo, 100, param_a, 1000)
export_a_partition(dados, id_rotulo, 100, param_a, 2000)
export_a_partition(dados, id_rotulo, 100, param_a, 3000)
export_a_partition(dados, id_rotulo, 200, param_a, 1000)
export_a_partition(dados, id_rotulo, 200, param_a, 2000)
export_a_partition(dados, id_rotulo, 200, param_a, 3000)
export_a_partition(dados, id_rotulo, 320, param_a, 1000)
export_a_partition(dados, id_rotulo, 320, param_a, 2000)
export_a_partition(dados, id_rotulo, 320, param_a, 3000)
