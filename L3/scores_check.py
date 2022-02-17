import os
import pickle
import ast
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error

# Set directories
base_dir = os.getcwd()
model_dir = os.path.join(base_dir,'l3final.pkl')
data_dir = os.path.join(base_dir,'testdatafinal.csv')
scores_dir = os.path.join(base_dir,'l3finalscores.txt')

# get model
with open(model_dir, 'rb') as model_path:
    model = pickle.load(model_path)

# Read data and split
test_data = pd.read_csv(data_dir)
X = test_data.drop('sales', axis=1)
y = test_data['sales']

# Test model
preds = model.predict(X)
error = mean_squared_error(y, preds)
print(f'The MSE is {error}')

# Check for model drift
with open(scores_dir, 'r') as scores_path:
    scores = ast.literal_eval(scores_path.read())

UQ = np.percentile(scores, 75)
LQ = np.percentile(scores, 25)
IQR = UQ-LQ
print(f'The IQR is {IQR}')
print(error > (UQ + 1.5*IQR))




