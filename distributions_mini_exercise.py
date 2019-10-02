# Distributions Mini Exercise

# Use scipy statistical distribution to answer the questions below:

from scipy import stats
import numpy as np 

die_distribution = stats.randint(1,7)

# What is the probility of rolling a 1?

die_distribution.pmf(1)

# There's a 1 in 2 chance that I'll roll higher than what number?

die_distribution.sf(1/2)

# What is the probability of rolling less than or equal to 2?

die_distribution.cdf(2)

# There is a 5 in 6 chance that my roll will be less than or equal to what number?

die_distribution.ppf

