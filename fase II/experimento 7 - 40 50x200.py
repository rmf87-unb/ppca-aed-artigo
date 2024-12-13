import pandas as pd
import numpy as np
from scipy.optimize import linear_sum_assignment

# Step 1: Load the data
file_name = "dados_50_200.csv"
data = pd.read_csv(file_name, sep=';', header=None, names=["IDENTIFICADOR", "CARGO", "PERCENT_PRI", "DISTANCE_KM"])

# Step 2: Create the cost matrix
# Pivot the data to create a matrix where rows are employees and columns are positions
cost_matrix_percent = data.pivot(index="IDENTIFICADOR", columns="CARGO", values="PERCENT_PRI").fillna(np.inf).to_numpy()
cost_matrix_distance = data.pivot(index="IDENTIFICADOR", columns="CARGO", values="DISTANCE_KM").fillna(np.inf).to_numpy()

# Normalize the cost matrices (optional, for combined minimization)
cost_matrix_percent_norm = cost_matrix_percent / np.nanmax(cost_matrix_percent)
cost_matrix_distance_norm = cost_matrix_distance / np.nanmax(cost_matrix_distance)

# Combine the cost matrices (weighted sum)
w1, w2 = 0.5, 0.5  # Weights for PERCENT_PRI and DISTANCE_KM
cost_matrix_combined = w1 * cost_matrix_percent_norm + w2 * cost_matrix_distance_norm

# Step 3: Solve the assignment problem
# Choose the cost matrix to minimize: cost_matrix_percent, cost_matrix_distance, or cost_matrix_combined
cost_matrix = cost_matrix_combined  # Change this to the desired cost matrix
row_ind, col_ind = linear_sum_assignment(cost_matrix)

# Step 4: Calculate the total minimized cost
total_cost = cost_matrix[row_ind, col_ind].sum()

# Step 5: Output the results
assignments = list(zip(row_ind, col_ind))
print("Optimal Assignments (Employee -> Position):", assignments)
print("Total Minimized Cost:", total_cost)