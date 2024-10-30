# plot.py

import matplotlib.pyplot as plt


def plotting(data, centers, labels, PNG_name):
    # Plot the clusters
    plt.scatter(data['Height'], data['Weight'], c=labels)
    # Plot the centers
    plt.scatter(centers[:, 0], centers[:, 1], c='red')
    # Save the plot as a PNG file
    plt.savefig(str(PNG_name+'.png'))
    plt.close()