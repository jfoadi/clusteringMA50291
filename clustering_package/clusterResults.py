# clusterResults.py


def outputs(data, centers, labels):
    # Calculate the number of clusters
    n_clusters = len(centers)

    # Output STUFF
    print('Results from', str(n_clusters), 'clusters:')
    for i in range(n_clusters):
        print('Representative points: Height, Weight for Group ',i,':', centers[i])
    print('Number of pupils in each group:')
    for i in range(n_clusters):
        print(len(data[labels == i]))
    return None

