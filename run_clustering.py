# run_clustering.py

from clustering_package import ClusterOutputs, readFile


if __name__ == "__main__":
    # Get the data from the CSV file
    data = readFile('data_Borough_school.csv')

    # Try 2, 3, 4, 5 clusters
    for n_clusters in range(2, 6):
        print("\n\nRunning for", n_clusters, "clusters\n\n")
        # Get all relevant outputs
        ClusterOutputs(data, n_clusters, "kmeans_"+str(n_clusters)+"_Modular", str(n_clusters)+"_cluster")
