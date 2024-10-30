import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv('data_Borough_school.csv')

import data_chars as ch

mean1,median1,var1,std1 = ch.chars(data)

print(mean1, median1)