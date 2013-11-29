# This code will execute a command from the terminal.  It will call python and 
# mrjob to count the number of words in a given folder using mapreduce on Amazon 
# Web Services. It will also measure the execution time for each instances. 

import os
import subprocess
import numpy as np
import time

numInstances=np.array([[np.arange(4.,44,4)]])
timeMeasure=np.array(np.size(numInstances))
terCmd1="python word_count_mr.py -r emr"
terCmd3="s3://hafezbucketcloudcourse/TextFiles/txt/"
cnt=0
for count in numInstances: 
    terCmd2="--num-ec2-instances="+str(count)
    terCmd4="out"+str(count)+".txt"
    terCmd=terCmd1+terCmd2+terCmd3+terCmd4
    start=time.time()
    subprocess.call(terCmd.split())
    end=time.time()
    timeMeasure[cnt]=end-start
    
    
    
