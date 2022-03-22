import pandas as pd
data = pd.read_csv('https://raw.githubusercontent.com/Asma2442/data/main/SOCR-HeightWeight.csv')
weight= data['Weight(Pounds)']

import statistics
mean = statistics.mean(weight)
median = statistics.median(weight)
mode = statistics.mode(weight)
print(median, mean, mode)