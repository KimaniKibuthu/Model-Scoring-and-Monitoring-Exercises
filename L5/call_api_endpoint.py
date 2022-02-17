import subprocess
import requests

response1= subprocess.run(['curl', '127.0.0.1:8000?user=KK']).stdout
print(f'The first response id {response1}')

response2= subprocess.run(['curl', '127.0.0.1:8000/size?filename=testdata.csv']).stdout
print(f'The second response id {response2}')

response3= subprocess.run(['curl', '127.0.0.1:8000/summary?filename=testdata.csv']).stdout
print(f'The third response id {response3}')

response4= requests.get('127.0.0.1:8000?user=KK').content
print(f'The fourth response id {response4}')

response5= requests.get('127.0.0.1:8000/size?filename=testdata.csv').content
print(f'The fifth response id {response5}')

response6= requests.get('127.0.0.1:8000/summary?filename=testdata.csv').content
print(f'The sixth response id {response6}')

