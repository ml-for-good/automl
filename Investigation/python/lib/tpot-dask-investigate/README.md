Introduction:
Here is a script using tpot and dask to fine the best machine learning pipeline for data set iris.
Tpot classifier had been set three times with different parameters to test the performance.
In the first classifier, 'n_jobs' is set to be 1, which means tpot only use 1 core on this computer.
In the second classifier, 'n_jobs' is set to be -1, which means tpot will use all the cores on the computer.
In the third classifier, 'n_jobs' is set to be -1, and 'use_dask' is set ture, which means all cores will be used and dask is implemented.
Running time of the three methods will be printed on the screen when the training is over.
And the finded best pipeline will be saved in current dir, the file names are 
'tpot_iris_pipeline_1.py', 
'tpot_iris_pipeline_2.py' 
and 'tpot_dask_iris_pipeline.py'.

Prerequires:
$pip install tpot
$conda install dask
$conda install -c conda-forge dask-ml

To use the scripy:
$python .\tpot_with_dask_for_iris.py

More references:
http://epistasislab.github.io/tpot/
https://ml.dask.org/