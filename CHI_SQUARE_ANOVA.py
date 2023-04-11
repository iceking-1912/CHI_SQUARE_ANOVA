import numpy as np
from scipy.stats import f

# Data
sales = np.array([[4, 3, 2], [3, 5, 3], [4, 5, 6]]).T

# Define Null & Alternative Hypothesis
# H0: All means are equal
# H1: At least one mean is different

# Select Significance Level
alpha = 0.05

# Calculate Sum of all observations
T = np.sum(sales)

# Calculate correction factor
nT = sales.size
CF = T**2 / nT

# Calculate Sum of squares total
SST = np.sum(sales**2) - CF

# Calculate Sum of squares between columns
SSB = np.sum(np.sum(sales, axis=0)**2 / sales.shape[0]) - CF

# Calculate Sum of squares within columns
SSW = SST - SSB

# Calculate Mean of squares between groups
k = sales.shape[1]
MSB = SSB / (k - 1)

# Calculate Mean of squares within groups
n = sales.shape[0] * sales.shape[1]
MSW = SSW / (n - k)

# Calculate Fcal and Fcrit
Fcal = MSB / MSW
dfnum = k - 1
dfden = n - k
Fcrit = f.ppf(1 - alpha, dfnum, dfden)

print(Fcrit)

# Compare Fcal & Fcrit and make your statistical & managerial decision
if Fcal > Fcrit:
    print("There is a significant difference in sales made in 3 cities (rejected H0)")
else:
    print("There is no significant difference in sales made in 3 cities (accepted H0)")
