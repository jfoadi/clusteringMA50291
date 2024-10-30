# DoItAll.py

from clustering_package import(
    cluster,
    stats,
    plotting,
    outputs,
    exportToCSV
)


def ClusterOutputs(data, n_clusters, plot_name_base, CSV_name_base):
    mean, median, variance, std_dev = stats(data)
    print("====================================\n STATS \n====================================")
    print('Mean height:', mean['Height'])
    print('Mean weight:', mean['Weight'])
    print('Median height:', median['Height'])
    print('Median weight:', median['Weight'])
    print('St. Deviation height:', std_dev['Height'])
    print('St. Deviation weight:', std_dev['Weight'])
    print("====================================")


    centers, labels = cluster(data, n_clusters)

    plotting(data, centers, labels, plot_name_base)

    print("====================================\n CLUSTERING OUTPUTS \n====================================")
    outputs(data, centers, labels)
    print("====================================")
    exportToCSV(data, labels, n_clusters, CSV_name_base)


    return None