#kMEANS


# K-means clustering
import pandas as pd
from sklearn.cluster import KMeans


def clustering(n_clusters:list,data:pd.DataFrame):
    """ 
    Function to fit a kmeans clustering model
        args: 
            - n_cluster: a list with the number of clusters
            - data: The dataset to be clustirized
        outcome:
            - data_labels: data with the labels corresponding to the clusters
            - score: the silhoutte_score for each Kmeans
            - cluster_centers: a dictionary with all the clusters centers
    """
    # Score is a list in which the silhoutte will be stored
    score = []
    data_labels = data.copy()
    cluster_centers = {}

    for k in n_clusters:
        cluster = KMeans(n_clusters=k)
        cluster.fit(data)
        score.append(cluster.inertia_)
        data_labels[f'k{k}_labels'] = cluster.labels_
        cluster_centers[f'K{k}'] = cluster.cluster_centers_

    return data_labels,score, cluster_centers

