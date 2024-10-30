# run_clustering.py

from clustering_package import(
    cluster,
    readFile,
    stats,
    plotting,
    outputs,
    exportToCSV
)

if __name__ == "__main__":
    data = readFile('data_Borough_school.csv')

    mean, median, variance, std_dev = stats(data)

    print('Mean height:', mean['Height'])
    print('Mean weight:', mean['Weight'])
    print('Median height:', median['Height'])
    print('Median weight:', median['Weight'])
    print('St. Deviation height:', std_dev['Height'])
    print('St. Deviation weight:', std_dev['Weight'])

    n_clusters = 2

    centers, labels = cluster(data, n_clusters)

    plotting(data, centers, labels, "kmeans2_Modular")

    outputs(data, centers, labels)

    exportToCSV(data, labels, n_clusters, "cluster")
