# Dispersion means how spread out the data points are in a dataset.
# Measures of dispersion help us understand the variability, spread, or scatter of data.
# It tells us:
# Are the data points close to each other?
# Or are they widely scattered?

import statistics as stats
data = [10, 15, 20, 25, 30]

# 1. Range --Difference between the largest and smallest value (Range = Max − Min)
# use : Quick estimate of spread. Used to detect extremes or outliers fast.

range_value = max(data) - min(data)
print(f"Range: {range_value}")


# 2.Variance --Average of squared differences from the mean. 
# use : important for analytics, risk, finance
# formula :  variance = (x1 - mean)**2 + (x2 - mean)**2 +... + (xn - mean)**2 / N
# mean = 10 + 15 + 20 + 25+ 30 \ 5 = 20
#Population Variance = (10 - 20)**2 + (15-20)**2 + (20-20)**2 + (25-20)**2 + (30-20)**2 / 5 =  100 + 25 + 0 + 25 + 100 /5 = 250/5 = 50
#sample Variance = (10 - 20)**2 + (15-20)**2 + (20-20)**2 + (25-20)**2 + (30-20)**2 / 4 =  100 + 25 + 0 + 25 + 100 /4 = 250/4 = 62.5

# keypoints :
#  If the variance is small, data points are close to the mean (stable).
#  If the variance is large, data points are spread out (unstable).


population_variance = stats.pvariance(data)
print(f"Population Variance: {population_variance}")
sample_variance = stats.variance(data) 
print(f"sample Variance: {sample_variance}")

# 3. Standard Deviation	--Square root of variance 
# use : great for reporting, comparison
sample_sd = stats.stdev(data) 
print(f"Sample Standard Deviation: {sample_sd}")
population_sd = stats.pstdev(data)
print(f"Population Standard Deviation: {population_sd}")


# Mini project : "Sales Performance Analyzer"

sales = [500, 480, 300, 550, 320, 290]

sales_range = max(sales) - min(sales)
sales_variance = stats.variance(sales)
sales_std_deviation = stats.stdev(sales)

print(f"Sales Range: {sales_range}")
print(f"Sales Variance: {sales_variance}")
print(f"Sales Standard Deviation: {sales_std_deviation:.2f}")
