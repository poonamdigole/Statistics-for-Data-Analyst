# central tendancy of data using statistics  
# central tendancy use to fill missing values
# if there is outliers in data then we have to use median not mean
# mode most use in string type data

population = [34 ,  56 , 50 , 34 , 78, 90]
sample = [20 , 50 , 15 ]

# mean
# method 1
pop_mean = sum(population)/len(population)
sample_mean = sum(sample)/len(sample)

print(pop_mean)
print(sample_mean)

# method 2 numpy
import numpy as np

population_mean = np.mean(population)
sample_mean = np.mean(sample)
population_median = np.median(population)
print(population_mean)
print(sample_mean)
print(population_median)

# method 3 using statistics
import statistics as stats
pop_stats_mean = stats.mean(population)
print(pop_stats_mean)

pop_stats_median = stats.median(population)
print(pop_stats_median)

pop_stats_mode = stats.mode(population)
print(pop_stats_mode)

num = [ 7, 6, 5, 8, 6, 7, 8, 9]
mode = stats.mode(num)
print("mode :" ,mode)
multi_mode = stats.multimode(num)
print("multi mode :" ,multi_mode)
# mode can be multiple , its called multi mode.


# method 4 using pandas 
import pandas as pd

df = pd.DataFrame(
    {
        'values':[20 , 35, 60, 20 , 50, 22]
    }
)

print(df)

mean_pandas = df['values'].mean()
print(mean_pandas)

median_pandas = df['values'].median()
print( "median by pandas :" ,median_pandas)

mode_pandas = df['values'].mode()
print('mode by pandas : ' , mode_pandas)