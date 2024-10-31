def printresults(k, centres, labels, data):
    print(f'Results from {k} clusters:')
    for i in range(1,k+1):
        print(f'Representative points: Height, Weight for Group {i}:', centres[f'centre{k}'][i-1])
        print(f'Number of pupils in each group:', len(data[labels[f'label{k}'] == 0]),  len(data[labels[f'label{k}'] == 1]))
