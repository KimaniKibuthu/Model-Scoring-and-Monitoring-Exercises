import ast
import os
import numpy as np
import pandas as pd

# Directories
base_dir = os.getcwd()
data_dir = os.path.join(base_dir, 'samplefile2.csv')
mean_dir = os.path.join(base_dir, 'historicmeans.txt')

# Load data
with open(mean_dir, 'r') as f:
    historic_means = ast.literal_eval(f.read())
    
data = pd.read_csv(data_dir)

# Check for stability
current_means = list(data.mean())
percentage_change = [(current_means[i] - historic_means[i])/historic_means[i] for i in range(len(historic_means))]
                     
print(f'The percentage change is: {percentage_change}')
print(current_means)

nulls = [data[column].isnull().sum() for column in data.columns]

print(nulls)



