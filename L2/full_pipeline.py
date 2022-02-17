# Import the necessary libraries
import pandas as pd
import os

# State the directories
base_dir = os.getcwd()
data_dir = os.path.join(base_dir, 'sales.csv')
model_name = os.path.join(base_dir, 'model.pkl')

# Import the data
sales = pd.read_csv(data_dir)
print(len(sales))


    