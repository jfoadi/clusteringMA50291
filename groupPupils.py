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
from utils import loaddata, eda, clustering, visualization, insights
import yaml
import seaborn as sns

logging.basicConfig(filename='server-soap.1.log',
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(threadName)-10s %(message)s',)

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



logging.info("----------------------------------------------")
logging.info("Step 5: Printing results")
logging.info("----------------------------------------------")


insights.insights(cluster_centers=cluster_centers, data=data_labels, n_clusters=n_clusters)


logging.info("----------------------------------------------")
logging.info("Step 6: Exporting results")
logging.info("----------------------------------------------")

data_labels.to_csv('data_clusters.csv')     