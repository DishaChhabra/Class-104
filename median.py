import pandas as pd
data = pd.read_csv('https://raw.githubusercontent.com/Asma2442/data/main/SOCR-HeightWeight.csv')
height = data['Height(Inches)'].tolist()

height.sort()

n = len(height)

if n%2==0:
    #10/2 = 5 10//2 = remove decimal points like 9/2 = 4.5 9//2 = 4 float is for decimals the info is decimal but position is integer
    n1 = float(height[n//2])
    n2 = float(height[n//2+1])
    median = (n1+n2)/2
else:
    median = float(height[n//2])

print(median)

import statistics
median1 = statistics.median(height)
print(median1)