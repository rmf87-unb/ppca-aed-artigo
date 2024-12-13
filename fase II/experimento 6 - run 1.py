import pandas as pd
import numpy as np
from scipy.optimize import linear_sum_assignment

# Step 1: Load the data
file_path = "dados_50_50.csv"  # Replace with the correct file path
data = pd.read_csv(file_path, sep=";")

# Step 2: Prepare the cost matrices
# Convert PERCENT_PRI and DISTANCE_KM to numeric (replace commas with dots for decimals)
data["PERCENT_PRI"] = data["PERCENT_PRI"].str.replace(",", ".").astype(float)
data["DISTANCE_KM"] = data["DISTANCE_KM"].str.replace(",", ".").astype(float)

# Pivot the data to create cost matrices
employees = data["IDENTIFICADOR"].unique()
positions = data["CARGO"].unique()

# Create cost matrices for PERCENT_PRI and DISTANCE_KM
cost_percent_pri = data.pivot(
    index="IDENTIFICADOR", columns="CARGO", values="PERCENT_PRI"
).to_numpy()
cost_distance_km = data.pivot(
    index="IDENTIFICADOR", columns="CARGO", values="DISTANCE_KM"
).to_numpy()

# Normalize the cost matrices (optional, for combined optimization)
cost_percent_pri /= cost_percent_pri.max()
cost_distance_km /= cost_distance_km.max()

# Combine the costs (weighted sum)
w1, w2 = 0.5, 0.5  # Weights for PERCENT_PRI and DISTANCE_KM
combined_cost = w1 * cost_percent_pri + w2 * cost_distance_km

# Step 3: Solve the assignment problem
row_ind, col_ind = linear_sum_assignment(combined_cost)

# Step 4: Calculate the total minimized cost
total_cost = combined_cost[row_ind, col_ind].sum()

# Step 5: Display the results
assignments = pd.DataFrame(
    {
        "Employee": employees[row_ind],
        "Position": positions[col_ind],
        "Cost": combined_cost[row_ind, col_ind],
    }
)

print("Optimal Assignments:")
print(assignments)
print(f"Total Minimized Cost: {total_cost}")
