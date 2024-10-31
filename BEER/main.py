# Importing the packages needed
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importing the data
data = pd.read_csv('data_Borough_school.csv')

# Importing and using the data characteristics function I made 
import data_chars as ch
mean1,median1,var1,std1 = ch.chars(data)
chatactaristics = [mean1, median1, var1, std1]
# Now have the mean, median, variance and the standard deviation    

# Printing all of the relevent statistics
import getchars as gc
for col in data.columns:
    gc.getchars('mean', mean1, col)     
    gc.getchars('median', median1, col) 
    gc.getchars('variance', var1, col)          
    gc.getchars('standard diviation', std1, col)
