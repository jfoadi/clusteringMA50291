# Exploratory data analysis

# Importing necessary libraries
import pandas as pd
import numpy as np
import logging 
logging.basicConfig(level=logging.INFO)

# Function to compute descriptive statistics
def descriptive_sts(data:pd.DataFrame)-> pd.DataFrame:
    """ This function generates a data frame with the descriptive statistics of the data
        args:
            data: pandas data frame with the information of interest
        outcome:
            pandas data frame with the statistics
    """
    # Calculating mean
    mean = data.mean()
    # Calculating median
    median = data.median()
    # Calculating variance
    variance = data.var()
    # Calculating standard deviation
    std_dev = data.std()
    df = pd.DataFrame([mean,median,variance,std_dev],index=["Mean","Median","Variance","std_dev"])
    return df