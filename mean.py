import pandas as pd
data = pd.read_csv('https://raw.githubusercontent.com/Asma2442/data/main/SOCR-HeightWeight.csv')
height = data['Height(Inches)'].tolist()
sum = 0
for i in height:
    sum=sum+i

mean = sum/len(height)
print(mean)

import statistics
mean2 = statistics.mean(height)
print(mean2)