# kmeans.py

# K-means clustering
from sklearn.cluster import KMeans

def cluster(data, n_clusters = 2):
    # Creates the KMeans object
    kmeans = KMeans(n_clusters)

    # Fit the data
    kmeans.fit(data)

    # Get the centers
    centers = kmeans.cluster_centers_

    # Get the labels
    labels = kmeans.labels_

    # Output the centers and labels
    return centers, labels