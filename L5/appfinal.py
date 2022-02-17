import pickle
import pandas as pd
from flask import Flask, request

# Instantiate app
app = Flask(__name__)

def read_pickle(modelname):
    with open(modelname, 'rb') as f:
        model = pickle.load(f)
    return model

def read_data(dataname):
    data = pd.read_csv(dataname)
    return data
        

# Instantiate endpoints
@app.route('/predictions')
def predictor():
    dataname = request.args.get('dataname')
    modelname = request.args.get('modelname')
    
    data = read_data(dataname)
    model = read_pickle(modelname)
    
    predictions = model.predict(data)
    return str(predictions)

app.run(host='0.0.0.0', port=8000)