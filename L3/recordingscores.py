import ast
import os
import pandas as pd
import numpy as np

recent_r2=0.6
recent_sse=52938


#record a score in a DataFrame
base_dir = os.getcwd()
scores_dir = os.path.join(base_dir, 'previousscores.csv')

previous_scores = pd.read_csv(scores_dir)

#find the maximum version number
max_version = max(previous_scores['version'].values)
print(f'The max version is {max_version}')
#generate rows
new_r2_row = {'metric':'r2', 'version': max_version+1, 'score':recent_r2}

new_sse_row = {'metric':'sse', 'version': max_version+1, 'score':recent_sse}

#write the dataset to a csv
if recent_r2 > previous_scores.loc[previous_scores['metric'] == 'r2', 'score'].max():
    print('New r2 is greater')
    previous_scores.append(new_r2_row, ignore_index=True)
elif recent_sse < previous_scores.loc[previous_scores['metric'] == 'sse', 'score'].min():
    print('new sse is less')
    previous_scores.append(new_sse_row, ignore_index=True)
    
previous_scores.to_csv(os.path.join(base_dir,'new_scores.csv'))

