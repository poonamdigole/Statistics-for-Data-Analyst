# Data Representation : charts , graphs , table, frequency distribution 

# 1. Normal distribution
# A normal distribution is a symmetrical, bell-shaped distribution where most of the data points are concentrated around the mean. In this distribution, the mean, median, and mode are equal
# Used for: Modeling natural phenomena like height, IQ, measurement errors, etc.

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data_normal = np.random.normal(loc=50, scale=10, size=1000)
# loc = mean (center), scale = standard deviation (spread), size = number of points
sns.histplot(data_normal, kde=True, color='orange')
plt.title("Normal Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# 2. Skewed Distribution
# A skewed distribution is an asymmetrical distribution where data points are stretched more on one side of the mean.
# Positive skew: Tail is on the right (e.g., income). Mean>median>mode
# Negative skew: Tail is on the left (e.g., age of retirement). Mean<Median<Mode
# Used for: Identifying imbalance in data, preparing for transformations.

# Positive Skew
data_skewed = np.random.exponential(scale=2, size=1000)
# The exponential used to model the time between independent events
sns.histplot(data_skewed, kde=True , color='red')
plt.title("Positively Skewed Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# Negative Skew
data_skewed = -np.random.exponential(scale=2, size=1000)
sns.histplot(data_skewed, kde=True , color='purple')
plt.title("Negatively Skewed Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# 3. Uniform Distribution
# A uniform distribution is where all outcomes are equally likely, resulting in a flat, constant probability across a range.
data_uniform = np.random.uniform(low=10, high=20, size=1000)

sns.histplot(data_uniform, kde=True, color='green')
plt.title("Uniform Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()


# 4. Bimodal Distribution
# Two peaks (modes), Might indicate two different groups
# Use :Identifying sub-populations in survey data, test scores, user behavior analysis.
data1 = np.random.normal(loc=20, scale=3, size=500)
data2 = np.random.normal(loc=40, scale=3, size=500)
data_bimodal = np.concatenate([data1, data2])

sns.histplot(data_bimodal, kde=True, color='Pink')
plt.title("Bimodal Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()


# 5.  Multimodal Distribution
# More than two peaks
# Can occur in complex datasets
# Use :Clustering analysis, market segmentation, detecting mixed data sources.
d1 = np.random.normal(20, 2, 300 )
d2 = np.random.normal(40, 2, 300 )
d3 = np.random.normal(60, 2, 300 )
data_multi = np.concatenate([d1, d2, d3])

sns.histplot(data_multi, kde=True , color='blue')
plt.title("Multimodal Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
