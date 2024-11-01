from sklearn.cluster import KMeans    # type: ignore

def mykmeans(n, data):
    allkmeans = {}
    allcentres = {}
    alllabels = {}
    for i in range(2,n+1):
        kmean = KMeans(n_clusters=i)
        kmean.fit(data)
        allkmeans['kmeans{0}'.format(i)] = kmean
        allcentres['centre{0}'.format(i)] = kmean.cluster_centers_
        alllabels['label{0}'.format(i)] = kmean.labels_
    return allkmeans, allcentres, alllabels
