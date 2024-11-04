# Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Reading the csv file
data = pd.read_csv('data_Borough_school.csv')

print(f"""Mean:  
{data.mean().to_string()}
      
Median:  
{data.median().to_string()}

Variance:  
{data.var().to_string()}

Standard Deviation: 
{data.std().to_string()}

Units = cm, kg
""")

#make an empty score list
score_list = []

# Loop to find the best number of clusters
for n in range(2,12):
      kmeans = KMeans(n_clusters=n)
      kmeans.fit(data)
      center = kmeans.cluster_centers_
      labels = kmeans.labels_
      new_score = kmeans.score(data)
      score_list.append(new_score)
      print(f"cluster score k = {n}: {kmeans.score(data)}")

# Plotting the score list
plt.plot(range(2,12), score_list)
plt.savefig('score_list.png')
plt.close()

# by sight, the best number of clusters is 8 based on the elbow point of the score list plot
best_k = 9
kmeans = KMeans(n_clusters=best_k)
kmeans.fit(data)
center = kmeans.cluster_centers_
labels = kmeans.labels_
      
# Plotting the clusters into PNG file
plt.scatter(data['Height'], data['Weight'], c=labels)
plt.scatter(center[:, 0], center[:, 1], c='red')
plt.savefig('kmeans.png')
plt.close()

# printing out the cluster information
print(f'Results from {best_k} clusters:')
for i in range(best_k):
      print(f'Representative points: Height, Weight for Group {i+1}: {center[i]}')

# printing out the number of pupils in each cluster
print(f'Number of pupils in each group: {[len(data[labels==i]) for i in range(best_k)]}')
