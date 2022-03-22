import pandas as pd
data = pd.read_csv('https://raw.githubusercontent.com/Asma2442/data/main/SOCR-HeightWeight.csv')
height = data['Height(Inches)']

mode = height.value_counts()
print(mode)

import statistics
mode1 = statistics.mode(height)
print(mode1)