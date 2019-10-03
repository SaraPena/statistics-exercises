# Do your work for this exercise in either a python script named propabilty_distributions.py or a jupyter notebook notebook named probability_distributions.ipynb.

%matplotlib inline
import matplotlib.pyplot as plt  
import numpy as np 
from scipy import stats   
import random

np.random.seed(3)

# For the following problems, use python to simulate the problem and calculate an experimental probability, then compare that to the theoretical probability.

# 1. A bank found the average number of cars waiting during the noon hour at a drive up window follows a Poisson distribution with a mean of 2 cars. 
#    Make a chart of this distribution and answer these questions concerning the probability of cars waiting at the drive-up window.

n =  20000

sum([round(random.expovariate(.5)) == 0 for i in range(0,n)])/n


sum([random.choice([1,2,3,4,5,6]) == random.choice([1,2,3,4,5,6]) for i in range(0,n)])/n


sum([np.random.choice([False, True],8).sum() > 3 for i in range(0,n)])/n

data_science_student = (np.random.random(2) < .25).sum()
data_science_student.sum()

sum([(np.random.random(2) < .25).sum() == 5.0 for i in range(0,10000)])/10000

def consumption(mean,std,days):
    pt_consumption = np.round(np.random.normal(mean,std,days))
    pt_consumption = np.where(pt_consumption < 0, 0, pt_consumption)
    return np.int_(pt_consumption.sum())


sum([consumption(3,1.5,5) < 17 for i in range(0,n)])/n

def m_height(mean, std):
    return np.random.normal(mean, std)

def f_height(mean,std):
    return np.random.normal(mean, std)

sum([m_height(178, 8) < f_height(170,6) for i in range(0,10000)])/10000

p_corruption = 1/250

sum([sum(np.random.random(size = 50) < p_corruption) == 0 for i in range(0,n)])/n


# 2. Grades of State Univeristy graduates are normally distributed with a mean of 3.0 and a standard deviation of .3.
#    Calculate the following:
#    What grade point average is required to be in the top 5% of the graduating class?

average_grade = 3.0
std = .3

n_simulations = nrows = 1000

grade_distribution = stats.norm(average_grade,std).rvs((10000,700))

grade_distribution.shape

np.percentile(grade_distribution, 95, axis = 1).mean()

stats.norm(average_grade, std).isf(.05)





