import pickle
import os
import pandas as pd
from sklearn.metrics import f1_score

# paths
base_dir = os.getcwd()
data_dir = os.path.join(base_dir, 'testdata.csv')
model_dir = os.path.join(base_dir, 'samplemodel.pkl')

# Read in data and model
test_data = pd.read_csv(data_dir)
print(f'The length of the data is {len(test_data)}')

with open(model_dir, 'rb') as model_path:
    model = pickle.load(model_path)
    
# Score the model
X = test_data.drop('col3', axis=1)
y = test_data['col3']

predictions = model.predict(X)
print(predictions)
score = f1_score(y, predictions)

print(f'The f1_score of the model is {score}')
      

