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

# Reading the csv file
data = pd.read_csv('data_Borough_school.csv')

## ADDING BEER 

# Calculating mean
mean = data.mean()

# Calculating median
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
kmeans2 = KMeans(n_clusters=2)
kmeans3 = KMeans(n_clusters=3)
kmeans4 = KMeans(n_clusters=4)
kmeans5 = KMeans(n_clusters=5)

# Fitting the data
kmeans2.fit(data)
kmeans3.fit(data)
kmeans4.fit(data)
kmeans5.fit(data)

# Getting the cluster centers
centers2 = kmeans2.cluster_centers_
centers3 = kmeans3.cluster_centers_
centers4 = kmeans4.cluster_centers_
centers5 = kmeans5.cluster_centers_

# Getting the labels
labels2 = kmeans2.labels_
labels3 = kmeans3.labels_
labels4 = kmeans4.labels_
labels5 = kmeans5.labels_

# Plotting the clusters into separate PNG files
plt.scatter(data['Height'], data['Weight'], c=labels2)
plt.scatter(centers2[:, 0], centers2[:, 1], c='red')
plt.savefig('kmeans2.png')
plt.close()

plt.scatter(data['Height'], data['Weight'], c=labels3)
plt.scatter(centers3[:, 0], centers3[:, 1], c='red')
plt.savefig('kmeans3.png')
plt.close()

plt.scatter(data['Height'], data['Weight'], c=labels4)
plt.scatter(centers4[:, 0], centers4[:, 1], c='red')
plt.savefig('kmeans4.png')
plt.close()

plt.scatter(data['Height'], data['Weight'], c=labels5)
plt.scatter(centers5[:, 0], centers5[:, 1], c='red')
plt.savefig('kmeans5.png')
plt.close()

# Print on screen results for 2 clusters
print('Results from 2 clusters:')
print('Representative points: Height, Weight for Group 1:', 
      centers2[0])
print('Representative points: Height, Weight for Group 2:', 
      centers2[1])
print('Number of pupils in each group:', len(data[labels2 == 0]), 
      len(data[labels2 == 1]))

# Print on screen results for 3 clusters
print('Results from 3 clusters:')
print('Representative points: Height, Weight for Group 1:', 
      centers3[0])
print('Representative points: Height, Weight for Group 2:',
      centers3[1])
print('Representative points: Height, Weight for Group 3:',
      centers3[2])
print('Number of pupils in each group:', len(data[labels3 == 0]),
      len(data[labels3 == 1]), len(data[labels3 == 2]))

# Print on screen results for 4 clusters
print('Results from 4 clusters:')
print('Representative points: Height, Weight for Group 1:', 
      centers4[0])
print('Representative points: Height, Weight for Group 2:',
      centers4[1])
print('Representative points: Height, Weight for Group 3:',
      centers4[2])
print('Representative points: Height, Weight for Group 4:',
      centers4[3])
print('Number of pupils in each group:', len(data[labels4 == 0]),
      len(data[labels4 == 1]), len(data[labels4 == 2]),
      len(data[labels4 == 3]))

# Print on screen results for 5 clusters
print('Results from 5 clusters:')
print('Representative points: Height, Weight for Group 1:', 
      centers5[0])
print('Representative points: Height, Weight for Group 2:',
      centers5[1])
print('Representative points: Height, Weight for Group 3:',
      centers5[2])
print('Representative points: Height, Weight for Group 4:',
      centers5[3])
print('Representative points: Height, Weight for Group 5:',
      centers5[4])
print('Number of pupils in each group:', len(data[labels5 == 0]),
      len(data[labels5 == 1]), len(data[labels5 == 2]),
      len(data[labels5 == 3]), len(data[labels5 == 4]))

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