# Print results

import pandas as pd 

def insights(cluster_centers:dict, data:pd.DataFrame, n_clusters:list):
    """
    Funtion to present results for each cluster
        args:
            - clusters_centers: dictionary with the cluster center points
            - data: data with the labels corresponding to each kmeans model
            - n_cluster: list with all the number of clusters desired
        outcome:
            Print the center points for each group of clusters and the counts of pupils according each grouo
    """
    
    for k,centers in zip(n_clusters,cluster_centers.values()):
        print(f"Results from {k} clusters")
        for kk in range(k):
            print(f'Representative points: Height, Weight for Group {kk+1}: {centers[kk]}')
        print(f"Number of pupils in each group: {data[f'k{k}_labels'].value_counts().sort_index()}")





