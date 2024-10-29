# getStats.py

def stats(data):
    # Calculating mean
    mean = data.mean()

    # Calculating median
    median = data.median()

    # Calculating variance
    variance = data.var()

    # Calculating standard deviation
    std_dev = data.std()

    # Returning the statistics
    return mean, median, variance, std_dev