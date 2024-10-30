# Description: This script reads a csv file with data about 
# height and weight of pupils in a school. It then calculates
# the mean, median, variance and standard deviation of the data.
# It also performs K-means clustering on the data and plots the
# clusters into separate PNG files. Finally, it prints on screen
# the results of the clustering.
# The csv file to test the program is 'data_Borough_school.csv'.

# Initial version: 2020-11-26 - James Foadi

# Importing necessary libraries
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import logging 
from utils import loaddata, eda, clustering, visualization
import yaml
import seaborn as sns
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Reading the parameters to be able to import the csv file
logging.info("----------------------------------------------")
logging.info("Step 1: Importing data process")
logging.info("----------------------------------------------")

with open('parameters/parameters.yaml', 'r') as file:
    parameters = yaml.safe_load(file)

filename = parameters['data']['filename']   
path = parameters['data']['path']
logging.info(f"The filepath is: {os.path.join(path,filename)}")
logging.info(f"Importing the data")
data = loaddata.load_data(filename, path)

logging.info("----------------------------------------------")
logging.info("Step 2: Descriptive and exploratory analysis")
logging.info("----------------------------------------------")

# Display a table with the descriptive statistics

logging.info("The descriptive statistics of the data are:")
print(eda.descriptive_sts(data))


logging.info("----------------------------------------------")
logging.info("Step 3: Clustering: Fitting Kmeans")
logging.info("----------------------------------------------")

n_clusters = parameters['kmeans']['n_clusters']
data_labels, score, cluster_centers = clustering.clustering(n_clusters=n_clusters,data=data)


logging.info("----------------------------------------------")
logging.info("Step 4: Elbow method")
logging.info("----------------------------------------------")

sns_plot = sns.lineplot(x = n_clusters, y = score)
sns_plot.set_title('Elbow Method')
sns_plot.set_ylabel('Inertia')
sns_plot.set_xlabel('# clusters')
logging.info("Exporting elbow plot image")
plt.savefig("elbow_plot.png")

logging.info("----------------------------------------------")
logging.info("Step 4: Plotting process")
logging.info("----------------------------------------------")


visualization.kplot(data_labels,n_clusters=n_clusters,cluster_centers=cluster_centers)


# # Plotting the clusters into separate PNG files
# plt.scatter(data['Height'], data['Weight'], c=labels2)
# plt.scatter(centers2[:, 0], centers2[:, 1], c='red')
# plt.savefig('kmeans2.png')
# plt.close()

# plt.scatter(data['Height'], data['Weight'], c=labels3)
# plt.scatter(centers3[:, 0], centers3[:, 1], c='red')
# plt.savefig('kmeans3.png')
# plt.close()

# plt.scatter(data['Height'], data['Weight'], c=labels4)
# plt.scatter(centers4[:, 0], centers4[:, 1], c='red')
# plt.savefig('kmeans4.png')
# plt.close()

# plt.scatter(data['Height'], data['Weight'], c=labels5)
# plt.scatter(centers5[:, 0], centers5[:, 1], c='red')
# plt.savefig('kmeans5.png')
# plt.close()

# # Print on screen results for 2 clusters
# print('Results from 2 clusters:')
# print('Representative points: Height, Weight for Group 1:', 
#       centers2[0])
# print('Representative points: Height, Weight for Group 2:', 
#       centers2[1])
# print('Number of pupils in each group:', len(data[labels2 == 0]), 
#       len(data[labels2 == 1]))

# # Print on screen results for 3 clusters
# print('Results from 3 clusters:')
# print('Representative points: Height, Weight for Group 1:', 
#       centers3[0])
# print('Representative points: Height, Weight for Group 2:',
#       centers3[1])
# print('Representative points: Height, Weight for Group 3:',
#       centers3[2])
# print('Number of pupils in each group:', len(data[labels3 == 0]),
#       len(data[labels3 == 1]), len(data[labels3 == 2]))

# # Print on screen results for 4 clusters
# print('Results from 4 clusters:')
# print('Representative points: Height, Weight for Group 1:', 
#       centers4[0])
# print('Representative points: Height, Weight for Group 2:',
#       centers4[1])
# print('Representative points: Height, Weight for Group 3:',
#       centers4[2])
# print('Representative points: Height, Weight for Group 4:',
#       centers4[3])
# print('Number of pupils in each group:', len(data[labels4 == 0]),
#       len(data[labels4 == 1]), len(data[labels4 == 2]),
#       len(data[labels4 == 3]))

# # Print on screen results for 5 clusters
# print('Results from 5 clusters:')
# print('Representative points: Height, Weight for Group 1:', 
#       centers5[0])
# print('Representative points: Height, Weight for Group 2:',
#       centers5[1])
# print('Representative points: Height, Weight for Group 3:',
#       centers5[2])
# print('Representative points: Height, Weight for Group 4:',
#       centers5[3])
# print('Representative points: Height, Weight for Group 5:',
#       centers5[4])
# print('Number of pupils in each group:', len(data[labels5 == 0]),
#       len(data[labels5 == 1]), len(data[labels5 == 2]),
#       len(data[labels5 == 3]), len(data[labels5 == 4]))

# 
# Exporting the clusters to separate csv files
# Not happy about this! Please change as you think best.
#data[labels2 == 0].to_csv('cluster1.csv')
#data[labels2 == 1].to_csv('cluster2.csv')
#data[labels3 == 0].to_csv('cluster1.csv')
#data[labels3 == 1].to_csv('cluster2.csv')
#data[labels3 == 2].to_csv('cluster3.csv')
#data[labels4 == 0].to_csv('cluster1.csv')
#data[labels4 == 1].to_csv('cluster2.csv')
#data[labels4 == 2].to_csv('cluster3.csv')
#data[labels4 == 3].to_csv('cluster4.csv')
#data[labels5 == 0].to_csv('cluster1.csv')
#data[labels5 == 1].to_csv('cluster2.csv')
#data[labels5 == 2].to_csv('cluster3.csv')
#data[labels5 == 3].to_csv('cluster4.csv')
#data[labels5 == 4].to_csv('cluster5.csv')     