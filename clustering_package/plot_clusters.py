import matplotlib.pyplot as plt

def clusters_plot(data, labels, centers):
    x = data.iloc[:, 0]
    y = data.iloc[:, 1]
    plt.scatter(x, y, c=labels, cmap='viridis')
    plt.scatter(centers[:, 0], centers[:, 1], c='red')
    nr_clusters = len(centers)
    plt.savefig(f'kmeans{nr_clusters}.png')
    plt.close()