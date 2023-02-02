import warnings
import numpy as np
import datetime
import statsmodels.api as sm
import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet
import statistics
import itertools
import sys

def legacy_inference(inputdf):
    
    #Run your inference logic here
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
    filename = inputfilepath + 'predictions_input.csv'
    inputdata = pd.read_csv(str(filename))

    #call legacy inference code as a function
    outputdata=legacy_inference(inputdata)
    
    #write Output back
    outputfilename = outputfilepath+"predictions_output.csv"
    outputdata.to_csv(outputfilename, index=False)
    print("Completed Run")