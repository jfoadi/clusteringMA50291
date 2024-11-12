# Description: This script reads a csv file with data about 
# height and weight of pupils in a school. It then calculates
# the mean, median, variance and standard deviation of the data.
# It also performs K-means clustering on the data and plots the
# clusters into separate PNG files. Finally, it prints on screen
# the results of the clustering.
# The csv file to test the program is 'data_Borough_school.csv'.

# Initial version: 2020-11-26 - James Foadi

# Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn

import os
# Set the working directory to the Downloads folder
downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
os.chdir(downloads_path)
data = pd.read_csv("/Users/New User/Desktop/repository/clusteringMA50291/data_Borough_school.csv")

# Calculating mean
mean = data.mean()

# Ca
# 
# lculating median
median = data.median()

# Calculating variance
variance = data.var()

# Calculating standard deviation
std_dev = data.std()

# Printing the statistics
print('Mean height:', mean['Height'])
print('Mean weight:', mean['Weight'])
print('Median height:', median['Height'])
print('Median weight:', median['Weight'])
print('St. Deviation height:', std_dev['Height'])
print('St. Deviation weight:', std_dev['Weight'])

# K-means clustering
from sklearn.cluster import KMeans

# Creating KMeans objects. Try 2, 3, 4, 5 clusters

#define kmeans so that we can reuse for any value of data and number of clusters
def perform_kmeans(n_clusters, data):
      kmeans = KMeans(n_clusters=n_clusters)
      kmeans.fit(data)
      centers = kmeans.cluster_centers_
      labels = kmeans.labels_
      return centers, labels

def plot_clusters(data, centers, labels, filename):
    """Plot the clustered data and save the figure."""
    plt.scatter(data['Height'], data['Weight'], c=labels, cmap='viridis')
    plt.scatter(centers[:, 0], centers[:, 1], c='red', marker='x')
    plt.title("KMeans Clustering")
    plt.xlabel("Height")
    plt.ylabel("Weight")
    plt.savefig(filename)
    plt.close()

def print_cluster_info(data, centers, labels):
    print(f"Results from {len(centers)} clusters:")
    for i, center in enumerate(centers):
        print(f"Representative points: Height, Weight for Group {i + 1}: {center}")
        print(f"Number of pupils in Group {i + 1}: {len(data[labels == i])}")

def export_clusters_to_csv(data, labels, prefix='cluster'):
    for label in labels:
        filename = f"{prefix}{label + 1}.csv"
        data[labels == label].to_csv(filename, index=False)
        print(f"Cluster {label + 1} exported to {filename}")

#create for loop to display kmeans data 2,3,4,5 as
for i in range(2,6):
      centers, labels = perform_kmeans(i, data)
      plot_clusters(data, centers, labels, f'kmeans{i}.png')
      print_cluster_info(data, centers, labels)
      export_clusters_to_csv(data, labels)

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