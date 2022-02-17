
from flask import Flask, request
import pandas as pd
import os

app = Flask(__name__)
def read_pandas(filename):
    data = pd.read_csv(filename)
    return data

@app.route('/')
def index():
    user = request.args.get('user')
    return "Hello " + user + '\n'

@app.route('/size')
def size_getter():
    filename = request.args.get('filename')
    data = read_pandas(filename)
    return str(len(data.index))


@app.route('/summary')
def summary_getter():
    filename = request.args.get('filename')
    data = read_pandas(filename)
    return str(data.mean())
    


app.run(host='0.0.0.0', port=8000)




