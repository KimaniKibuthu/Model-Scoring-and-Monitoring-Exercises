import subprocess

response = subprocess.run(['curl', '127.0.0.1:8000/predictions?dataname=predictiondata.csv&modelname=deployedmodel.pkl'], capture_output=True).stdout

print(f'The prediction is {response}')