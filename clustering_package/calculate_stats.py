def stats_calculator(data):
    mean = data.mean()
    median = data.median()
    variance = data.var()
    std_dev = data.std()
    return mean, median, variance, std_dev
