# Exploratory data analysis

# Importing necessary libraries
import os
import pandas as pd
import numpy as np
import logging 
logging.basicConfig(level=logging.INFO)


def load_data(filename:str,path:str, delimiter=None, ):
    """ Function to import data from csv files
        args:
            path: the directory where the file is stored
            filename: the name of the file
            delimiter: the delimir symbol. The default is None
        outcomes:
            pandas data frame with the imported information
    """
    file_path = os.path.join(path,filename)
    if not delimiter:
        return pd.read_csv(file_path)
    else:
        return pd.read_csv(file_path,sep=delimiter)
    
        

    