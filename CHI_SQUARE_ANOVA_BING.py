import scipy.stats as stats

def anova_two_way(data):
    # Define Null & Alternative Hypothesis
    # H0: No significant difference between the means of the groups
    # H1: There is a significant difference between the means of the groups
    
    # Select estimator & determine its distribution
    # We use F-distribution to test the hypothesis
    
    # Select Significance Level
    alpha = 0.05
    
    # Calculate Sum of all observations: T = Ʃxi
    T = sum([sum(row) for row in data])
    
    # Calculate correction factor: CF = T2 / nT where nT = sample size
    nT = len(data) * len(data[0])
    CF = T ** 2 / nT
    
    # Calculate Sum of squares columns, SSC = Σ((Σ𝑥𝑗)2/𝑛𝑖) − CF
    SSC = sum([sum(col) ** 2 / len(col) for col in zip(*data)]) - CF
    
    # Calculate Sum of squares rows, SSR = Σ((Σ𝑥𝑖)2/𝑛𝑗) − CF
    SSR = sum([sum(row) ** 2 / len(row) for row in data]) - CF
    
    # Calculate Sum of squares total, SST = Σ(Σ𝑥𝑖2) − CF
    SST = sum([sum([x ** 2 for x in row]) for row in data]) - CF
    
    # Calculate Sum of square error, SSE = SST – (SSC + SSR)
    SSE = SST - (SSC + SSR)
    
    # Calculate Mean of squares column, MSC = SSC / (c – 1)
    MSC = SSC / (len(data[0]) - 1)
    
    # Calculate Mean of squares rows, MSR = SSR / (r – 1)
    MSR = SSR / (len(data) - 1)
    
    # Calculate Mean of squares error, MSE = SSE / (c – 1)(r – 1)
    MSE = SSE / ((len(data[0]) - 1) * (len(data) - 1))
    
    # Calculate Fcal = MSC/MSE & MSR/MSE
    Fcal_col = MSC / MSE
    Fcal_row = MSR / MSE
    
    # Calculate Fcrit = F(dfnum, dfden, α) where dfnum = c-1 or r-1, dfden = (c-1)(r-1)
    dfnum_col, dfnum_row = len(data[0]) - 1, len(data) - 1
    dfden_col_row = (len(data[0]) - 1) * (len(data) - 1)
    
    Fcrit_col_row = stats.f.ppf(1 - alpha/2, dfnum_col, dfden_col_row)
    
    # Compare Fcal & Fcrit and make your statistical & managerial decisions 
    if Fcal_col > Fcrit_col_row:
        print("Reject H0 for columns")
        print("There is a significant difference between the means of the columns")
        
        if Fcal_row > Fcrit_col_row:
            print("Reject H0 for rows")
            print("There is a significant difference between the means of the rows")
        else:
            print("Fail to reject H0 for rows")
            print("There is no significant difference between the means of the rows")
            
    else:
        print("Fail to reject H0 for columns")
        print("There is no significant difference between the means of the columns")
        
        if Fcal_row > Fcrit_col_row:
            print("Reject H0 for rows")
            print("There is a significant difference between the means of the rows")
        else:
            print("Fail to reject H0 for rows")
            print("There is no significant difference between the means of the rows")
    print(Fcrit_col_row)
    print(Fcal_col)
    print(Fcal_row)

data = [[4,3,4],[3,2,5],[5,3,6]]

anova_two_way(data)
