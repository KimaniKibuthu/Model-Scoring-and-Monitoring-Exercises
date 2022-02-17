import os
import pandas as pd

# Specify directories
directories = ['data1', 'data2', 'data3']

# Specify locations
base_dir = os.getcwd()
print(base_dir)
output_location = os.path.join(base_dir, 'result.csv')

def data_aggregator(directories):
    global base_dir
    data = pd.DataFrame()
    for directory in directories:
        folder_path = os.path.join(base_dir, directory)
        files = os.listdir(folder_path)
        for file in files:
            file_path = os.path.join(folder_path, file)
            extension = file.split(sep='.')[-1]
            if extension == 'csv':
                temp_data = pd.read_csv(file_path)
                data = data.append(temp_data)
            elif extension == 'json':
                temp_data = pd.read_json(file_path)
                data = data.append(temp_data)
                
    return data

def data_cleaner(directories):
    global output_location
    data = data_aggregator(directories)
    # drop duplicates
    data = data.drop_duplicates()
    data.to_csv(output_location)
    
if __name__ == '__main__':
    data_cleaner(directories)


    
    
                     
                           