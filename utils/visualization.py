
# Visualization

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Plotting the clusters into separate PNG files


def kplot(data:pd.DataFrame, n_clusters:list,cluster_centers:dict):

    for k,centers in zip(n_clusters,cluster_centers.values()):
        
        var = f"k{k}_labels"
        plt.scatter(data['Height'], data['Weight'], c=data[var])
        plt.scatter(centers[:, 0], centers[:, 1], c='red')
        plt.savefig(f'kmeans{k}.png')
        plt.close()
    