#Pre-processing script that can run with SageMaker SKLearn training container in script mode
import warnings
from datetime import datetime
from dateutil.relativedelta import relativedelta
import numpy as np
import datetime
import pandas as pd
from datetime import datetime
import sys


def legacy_postprocessing(inputdf):
    
    #Pre-process your data
    outputdf=inputdf
    return(outputdf)

#main function to start the execution    
if __name__ == "__main__":
    
    print("Started Run")
    #make the script usable for local testing
    if len(sys.argv) > 1:
        inputtype = sys.argv[1]
        localpath = sys.argv[2]
    else:
        inputtype = ""
        localpath = ""
    
    if inputtype == "local":
        inputfilepath = localpath
        outputfilepath = localpath
    else: 
        #SM processing container's default input/output paths
        inputfilepath = '/opt/ml/processing/input/'
        outputfilepath = '/opt/ml/processing/output/'
    
    #read Input file
    filename = inputfilepath + 'predictions_ouput.csv'
    inputdata = pd.read_csv(str(filename))

    #Plug-in your legacy code here or call any functions
    #Postprocess your data
    outputdata=legacy_postprocessing(inputdata)
    
    #write Output back
    outputfilename = outputfilepath+"final_output.csv"
    outputdata.to_csv(outputfilename, index=False)
    print("Completed Run")