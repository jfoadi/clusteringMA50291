def printresults(k, centres, labels, data):
    print('')
    print('')
    print(f'RESULTS FOR {k} CLUSTERS:')
    for i in range(1,k+1):
        print(f'> Representative points: Height, Weight for Group {i}:', centres[f'centre{k}'][i-1])

    print('')
    print('Number of pupils in each group:')
    for i in range(k):
        print(f'> Group {i+1}:', len(data[labels[f'label{k}'] == i]))
