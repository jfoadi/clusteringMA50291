import pandas as pd
from clustering_package import (load_data, stats_calculator, print_stats, kmeans, clusters_plot, print_results)
if __name__ == '__main__':
    data = load_data('data_Borough_school.csv')
    mean, median, var, std_dev = stats_calculator(data)
    print_stats(data, mean, median, std_dev)
    for i in range(2, 6):
        centers, labels = kmeans(i, data)
        clusters_plot(data, labels, centers)
        print_results(data, labels, centers)