
import os
import timeit
import numpy as np
import ingestion
import training

# Timings
def ingestion_timing():
    start_time = timeit.default_timer()
    ingestion
    #os.system('ingestion.py')
    end_time = timeit.default_timer()
    timing = end_time - start_time
    #print(f'The time taken is {timing}') 
    return timing

def training_timing():
    start_time = timeit.default_timer()
    training
    #os.system('ingestion.py')
    end_time = timeit.default_timer()
    timing = end_time - start_time
    #print(f'The time taken is {timing}') 
    return timing

def measure_and_save_timings():
    ingestion_timings = []
    training_timings = []
    i = 0
    while i<20:
        ingestion_time = ingestion_timing()
        training_time = training_timing()
        ingestion_timings.append(ingestion_time)
        training_timings.append(training_time)
        i+=1
        
    ingestion_mean = np.mean(ingestion_timings)
    ingestion_std = np.std(ingestion_timings)
    ingestion_min = min(ingestion_timings)
    ingestion_max = max(ingestion_timings)
    
    training_mean = np.mean(training_timings)
    training_std = np.std(training_timings)
    training_min = min(training_timings)
    training_max = max(training_timings)
    
    timing_list = [ingestion_mean, ingestion_std, ingestion_min, ingestion_max, training_mean, training_std, training_min, training_max]
    
    print(timing_list)
    
measure_and_save_timings()       
