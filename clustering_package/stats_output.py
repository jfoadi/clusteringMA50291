def print_stats(data, mean, median, std_dev):
    for column in data.columns:
        print('Mean', column + ':', mean[column])
        print('Median', column + ':', median[column])
        print('St. Deviation', column + ':', std_dev[column])
