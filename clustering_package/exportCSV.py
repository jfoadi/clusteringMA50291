# exportCSV.py

def exportToCSV(data, labels, n_clusters, baseName):
    for i in range(n_clusters):
        # for each cluster, export all the data points from that cluster to a separate CSV file
        data[labels == i].to_csv("CSV_Outputs/" + baseName + str(i) + '.csv')
    return None