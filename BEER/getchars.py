def getchars(name, char, column):
    if column == 'Weight' or column == 'Height':
        return print(column + ' ' + name + ': ', char[column])
    else:
        return print('Unexpected characteristic or column name provided')
#print(column + ' ' + name + ': ')
