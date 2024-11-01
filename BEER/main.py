# Importing the python packages needed
import pandas as pd   # type: ignore
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans    # type: ignore

# Importing my functions from the files in the directory
import data_chars as data_chars
import getchars as getchars
import kmeans as km
import printresults as printresutls


##################
#     INPUTS     #

# Choose highest number of clusters to go up to
j = 5

# Enter the file path of the data
path = 'data_Borough_school.csv'

##################



# Importing the data
data = pd.read_csv(path)


# Calculating the mean, median, variance and the standard deviation    
mean1,median1,var1,std1 = data_chars.chars(data)


# Printing all of the relevent statistics
for col in data.columns:
    getchars.getchars(mean1, median1, var1, std1, col, data)

# Calculating the KMeans information to be plotted
allkmeans, allcentres, alllabels = km.mykmeans(j, data)

# Plotting the KMeans data for each number of clusters
for j in range(2,j+1):
    plt.scatter(data['Height'], data['Weight'], c=alllabels[f'label{j}'])
    plt.scatter(allcentres[f'centre{j}'][:,0], allcentres[f'centre{j}'][:,1], c='red')
    plt.savefig(f'kmeans{j}.png')
    plt.close()

# Printing the results of the KMeans for each number of clusters
print('')
print('RESULTS:')
for k in range(2,j+1):
    printresutls.printresults(k,allcentres,alllabels,data)
 