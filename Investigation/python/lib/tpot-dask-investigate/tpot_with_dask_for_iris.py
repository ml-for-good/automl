import dask.array as da
from tpot import TPOTClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np
from dask.distributed import Client, LocalCluster

import time

#load data
iris = load_iris()
#split training set and test set
X_train, X_test, y_train, y_test = train_test_split(iris.data, 
    iris.target, train_size=0.75, test_size=0.25, random_state=42)

#set simple tpot method on single core
tpot = TPOTClassifier(generations=5, population_size=50, verbosity=2, random_state=42, n_jobs=1, use_dask=False)
time_start = time.time()
#use tpot to train
tpot.fit(X_train, y_train)
time_end = time.time()
print("time to use tpot on 1 core without dask is ", time_end - time_start, " s.\n")

print("Fitting score : ", tpot.score(X_test, y_test))
tpot.export('tpot_iris_pipeline_1.py')

#set simple tpot method on multi core
tpot = TPOTClassifier(generations=5, population_size=50, verbosity=2, random_state=42, n_jobs=-1, use_dask=False)
time_start = time.time()
#use tpot to train
tpot.fit(X_train, y_train)
time_end = time.time()
print("time to use tpot on cores without dask is ", time_end - time_start, " s.\n")

print("Fitting score : ", tpot.score(X_test, y_test))
tpot.export('tpot_iris_pipeline_2.py')

#set dask client
client = Client(LocalCluster(processes=False, threads_per_worker=1, n_workers=4))

#set tpot method with dask
tpot_d = TPOTClassifier(generations=5, population_size=50, verbosity=2, random_state=42, n_jobs=-1, use_dask=True)
time_start = time.time()
#use tpot to train
tpot_d.fit(X_train, y_train)
time_end = time.time()
print("time to use tpot on cores with dask is ", time_end - time_start, " s.\n")

print("Fitting score : ", tpot_d.score(X_test, y_test))
tpot_d.export('tpot_dask_iris_pipeline.py')
