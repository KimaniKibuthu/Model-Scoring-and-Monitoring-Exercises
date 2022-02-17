import ast
import os
import numpy as np

newr2=0.3625
 
# Set directories
scores_dir = os.path.join(os.getcwd(),'previousscores.txt')

# Get data
with open(scores_dir, 'r') as f:
    scores = ast.literal_eval(f.read())
    
# Minimum
print(f'The min number is {min(scores)}')

if newr2 > max(scores):
    print('The R2 is fine')
elif newr2 < min(scores):
    print('The model is drifting')
    
print(f'The standard deviation is {np.std(scores)}')

print(newr2 < (np.mean(scores)-(2*np.std(scores))))

IQR = np.percentile(scores, 75) - np.percentile(scores, 25)
print(f'The IQR is {IQR}')

print(newr2 < (np.percentile(scores, 25) - (1.5 * IQR)))