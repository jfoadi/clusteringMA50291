# Importing the python packages needed
import pandas as pd   # type: ignore
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans    # type: ignore

# Importing my functions from the files in the directory
import data_chars as ch
import getchars as gc
import kmeans as km
import printresults as pr

# Importing the data
data = pd.read_csv('data_Borough_school.csv')

# Choose highest number of clusters to go up to
j = 5

mean1,median1,var1,std1 = ch.chars(data)
chatactaristics = [mean1, median1, var1, std1]
# Now have the mean, median, variance and the standard deviation    


# Printing all of the relevent statistics
for col in data.columns:
    gc.getchars('mean', mean1, col)     
    gc.getchars('median', median1, col) 
    gc.getchars('variance', var1, col)          
    gc.getchars('standard diviation', std1, col)


allkmeans, allcentres, alllabels = km.mykmeans(j, data)

for j in range(2,j+1):
    plt.scatter(data['Height'], data['Weight'], c=alllabels[f'label{j}'])
    plt.scatter(allcentres[f'centre{j}'][:,0], allcentres[f'centre{j}'][:,1], c='red')
    plt.savefig(f'kmeans{j}.png')
    plt.close()

for k in range(2,j+1):
    pr.printresults(k,allcentres,alllabels,data)