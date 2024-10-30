from sklearn.cluster import KMeans

def kmeans(n_clusters, data):
    kmeans = KMeans(n_clusters=n_clusters)
    kmeans.fit(data)
    centers = kmeans.cluster_centers_
    labels = kmeans.labels_
    return centers, labels
