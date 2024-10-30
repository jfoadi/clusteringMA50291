def print_results(data, labels, centers):
    nr_clusters = len(centers)  
    print(f'Results from {nr_clusters} clusters:')

    for i in range(nr_clusters):
        print(f'Representative points: {data.columns} for Group {i+1}:', 
        centers[i])

    counts = [len(data[labels == i]) for i in range(nr_clusters)]
    print('Number of pupils in each group:', *counts)
        
       
