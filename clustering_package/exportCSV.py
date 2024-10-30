# exportCSV.py

def exportToCSV(data, labels, n_clusters, baseName):
    for i in range(n_clusters):
        data[labels == i].to_csv(baseName + str(i) + '.csv')
    return None