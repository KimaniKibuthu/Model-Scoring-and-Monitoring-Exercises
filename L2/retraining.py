import pickle
import pandas as pd
from sklearn.linear_model import LogisticRegression
import os

###################Reading Records#############
base_dir = os.getcwd()

with open(os.path.join(base_dir, 'deployedmodelname.txt'), 'r') as file_name:
    model_name = file_name.read()

with open(os.path.join(base_dir, 'datalocation.txt'), 'r') as file_name:
    location_name = file_name.read()



##################Re-training a Model#############
trainingdata = pd.read_csv(os.path.join(base_dir, location_name))

X=trainingdata.loc[:,['col1','col2']].values.reshape(-1, 2)
y=trainingdata['col3'].values.ravel()

logit=LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
                    intercept_scaling=1, l1_ratio=None, max_iter=100,
                    multi_class='auto', n_jobs=None, penalty='l2',
                    random_state=0, solver='liblinear', tol=0.0001, verbose=0,
                    warm_start=False)
                    
logit.fit(X,y)



############Pushing to Production###################
production_dir = os.path.join(base_dir, 'production')
with open(os.path.join(production_dir, model_name), 'wb') as file_path:
    pickle.dump(logit, file_path)







