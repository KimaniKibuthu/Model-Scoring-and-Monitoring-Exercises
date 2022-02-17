import ast
import os
import numpy as np
import pandas as pd

# Directories
base_dir = os.getcwd()
data_dir = os.path.join(base_dir, 'samplefile3.csv')

# Check null values
data = pd.read_csv(data_dir)

print(data.isnull().sum())
print(data.col1.mean())