import numpy as np
from scipy import stats

# Define Null & Alternative Hypothesis
# H0: There is no significant difference between the means of the groups
# Ha: There is a significant difference between the means of the groups

# Select estimator & determine its distribution
# The estimator is the sample mean and its distribution is normal

# Select Significance Level
alpha = 0.05

# Sample data in a two-way layout
data = np.array([[4,3,4],[3,2,5],[5,3,6]])

# Calculate Sum of all observations
T = np.sum(data)

# Calculate correction factor
nT = data.size
CF = T**2 / nT

# Calculate Sum of squares columns
SSC = np.sum(np.sum(data, axis=0)**2 / data.shape[0]) - CF

# Calculate Sum of squares rows
SSR = np.sum(np.sum(data, axis=1)**2 / data.shape[1]) - CF

# Calculate Sum of squares total
SST = np.sum(data**2) - CF

# Calculate Sum of square error
SSE = SST - (SSC + SSR)

# Calculate Mean of squares column
MSC = SSC / (data.shape[1] - 1)

# Calculate Mean of squares rows
MSR = SSR / (data.shape[0] - 1)

# Calculate Mean of squares error
MSE = SSE / ((data.shape[1] - 1) * (data.shape[0] - 1))

# Calculate Fcal for columns and rows
Fcal_columns = MSC/MSE
Fcal_rows = MSR/MSE

# Calculate Fcrit for columns and rows
Fcrit_columns = stats.f.ppf(1-alpha, data.shape[1]-1, (data.shape[1]-1)*(data.shape[0]-1))
Fcrit_rows = stats.f.ppf(1-alpha, data.shape[0]-1, (data.shape[1]-1)*(data.shape[0]-1))

print("Results of two-way ANOVA analysis:")
print("Fcal for columns (salesmen):", Fcal_columns)
print("Fcrit for columns (salesmen):", Fcrit_columns)
print("Fcal for rows (cities):", Fcal_rows)
print("Fcrit for rows (cities):", Fcrit_rows)

# Compare Fcal & Fcrit and make your statistical & managerial decisions
if Fcal_columns > Fcrit_columns:
    print("Reject null hypothesis for columns. There is a significant difference in sales made by the three salesmen.")
else:
    print("Fail to reject null hypothesis for columns. There is no significant difference in sales made by the three salesmen.")

if Fcal_rows > Fcrit_rows:
    print("Reject null hypothesis for rows. There is a significant difference in sales made in the three cities.")
else:
    print("Fail to reject null hypothesis for rows. There is no significant difference in sales made in the three cities.")