# DoItAll.py

from clustering_package import(
    cluster,
    stats,
    plotting,
    outputs,
    exportToCSV
)


def ClusterOutputs(data, n_clusters, plot_name_base, CSV_name_base):
    # Calculates all the relevant stats from the data and outputs them
    mean, median, variance, std_dev = stats(data)
    print("====================================\n STATS \n====================================")
    print('Mean height:', mean['Height'])
    print('Mean weight:', mean['Weight'])
    print('Median height:', median['Height'])
    print('Median weight:', median['Weight'])
    print('St. Deviation height:', std_dev['Height'])
    print('St. Deviation weight:', std_dev['Weight'])
    print("====================================")

    # clusters the data, giving us labels and the centers of the clusters
    centers, labels = cluster(data, n_clusters)

    # generates the plots of the data, coloured by the labels and with the centers marked
    plotting(data, centers, labels, plot_name_base)

    # outputs data about the centers locations and the number of points in each cluster
    print("====================================\n CLUSTERING OUTPUTS \n====================================")
    outputs(data, centers, labels)
    print("====================================")

    # exports the data from each cluster to separate CSV files
    exportToCSV(data, labels, n_clusters, CSV_name_base)


    return None