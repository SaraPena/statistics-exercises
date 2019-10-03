# Do your work for this exercise in either a python script named propabilty_distributions.py or a jupyter notebook notebook named probability_distributions.ipynb.

%matplotlib inline
import matplotlib.pyplot as plt  
import numpy as np 
from scipy import stats   
import random
import pandas as pd
from env import host, user, password

np.random.seed(3)

# For the following problems, use python to simulate the problem and calculate an experimental probability, then compare that to the theoretical probability.

# 1. A bank found the average number of cars waiting during the noon hour at a drive up window follows a Poisson distribution with a mean of 2 cars. 
#    Make a chart of this distribution and answer these questions concerning the probability of cars waiting at the drive-up window.

n_simulations =  10000

def distributions_example10():
    x = range(8)
    y = stats.poisson(2).pmf(x)

    plt.figure(figsize=(9, 6))
    plt.bar(x, y, edgecolor='black', color='white', width=1)
    plt.xticks(x)
    plt.ylabel('P(X = x)')
    plt.xlabel('lbs of coffee consumed')
    plt.bar(0, stats.poisson(2).pmf(0), width=1, color='darkseagreen', edgecolor='black')
    plt.annotate(f'P(X = 0) = {stats.poisson(2).pmf(0):.3f}', (0, stats.poisson(2).pmf(0)),
                 xytext=(3, .20), arrowprops={'arrowstyle': '->'})

distributions_example10()

# What is the probability that no cars drive up in the noon hour?
stats.poisson(2).pmf(0)

# Simulation:
sum([stats.poisson(2).rvs() == 0 for i in range(0,n_simulations)])/10000

# What is the probability that 3 or more cars come through the drive through?

stats.poisson(2).sf(2)

# Simulation:
sum([stats.poisson(2).rvs() > 2 for i in range(0,n_simulations)])/n_simulations

# How likely is it that the drive through gets at least 1 car?

stats.poisson(2).sf(0)

sum([stats.poisson(2).rvs() >= 1 for i in range(0,10000)])/10000

# 2. Grades of State Univeristy graduates are normally distributed with a mean of 3.0 and a standard deviation of .3.
#    Calculate the following:
#    What grade point average is required to be in the top 5% of the graduating class?
average_grade = 3.0
std = .3
students = 70

stats.norm(average_grade, std).isf(.05)

# Simulation:

def grades(average_grade,std,students): 
    grade_distribution = stats.norm(average_grade,std).rvs(students)
    return grade_distribution

grades(average_grade, std, students)

sum([np.percentile(grades(average_grade,std,students), 95) for i in range(0,n_simulations)])/n_simulations

#   What GPA constitutes the bottom 15% of the class?

stats.norm(average_grade,std).ppf(.15)

# Simulation:

sum([np.percentile(grades(average_grade,std,students), 15) for i in range(0,n_trials)])/n_trials

#   An eccentric alumnus left scholarship money for students in the third decile from the bottom of their class. Determine the range of the third decile. 
#   Would a student with 2.8 grade point average qualify for this scholarship?

stats.norm(average_grade,std).ppf(.21)
stats.norm(average_grade,std).ppf(.30)

# Simulation:

sum([np.percentile(grades(average_grade,std,students), 21) for i in range(0,n_trials)])/n_trials
sum([np.percentile(grades(average_grade,std,students), 30) for i in range(0,n_trials)])/n_trials

##


# 3. A marketing website has an average click-through rate of 2%. One day they observe 4326 visitors and 97 click-throughs.
#    How likely is it that this many people or more click through?

stats.binom(4326,.02).sf(96)

sum([stats.binom(4326,.02).rvs() > 96 for i in range(0,20000)])/20000


# 4. You are working on some statistics homework consisting of 100 questions where all of the answers are a probability rounded to the hundreths place.
#    Looking to save time, you put down random probabilities as the answer to each question.
#    - What is the probability that at least one of your first 60 answers is correct.

stats.binom(60, .01).sf(0)

# Simulation:
grade_key = np.random.random(60).round(2)

sum([(np.random.random(60).round(2) == grade_key).sum() >= 1 for i in range(0,n_trials)])/n_trials

sum([np.random.choice([0,1], 60, p=[.99,.01]).sum() >=1 for i in range(0,n_trials)])/n_trials

sum([stats.binom(60,.01).rvs() > 0 for i in range(0,n_trials)])/n_trials

# 5. The Codeup staff tends to get upset when the student break are is not cleaned up.
#    Suppose that there is a 3% chance taht any one student cleans the break area when they visit it.
#    On a given day about 90% of the 3 active chorts of 22 students vist the break area.
#    How likely is it that the break area gets cleaned up each day?
#    How likely is it that it goes two days without getting cleaned up? All week?

students_visit = .9*(3*22)

stats.binom(students_visit,.03).sf(0)

stats.binom(59,.03).sf(0)**5

stats.binom(59, .03).pmf(0)**2

sum([stats.binom(56,.03).rvs() > 0 for i in range(0,n_trials)])/n_trials

(stats.binom(56,.03).rvs(10000)>0).mean()

# 6. You want to get lunch at La Panaderia, but notice that then line is usually very long at lunchtime.
#    After several weeks of carful observation, you notice that the average number of people in line when your break starts is normally distributed with a mean of 15 and standard deviation of 3. 
#    If it takes 2 minutes for each person to order, and 10 minutes form ordering to get your food what is the likelihood that you will ahve at least 15 minutes left to eat before you have to go back to class?
#    Assume you have one hour for lunch, and ignore travel time to and from La Panaderia.

n_people = 17
n_minutes_for_lunch = 60 - 2*n_people - 10

mean = 15
std 3

stats.norm(15,3).cdf(17)

((stats.norm(15,3).rvs(10000)) <= 17).mean()

# 7. Connect to the employees database and find the average salary of current employees, along with the standard deviation.
#    Model the distribution of employees salaries wit hthe normal distribution, and answer the following questions:

def get_url(user, password, host, database):
    url = f'mysql+pymysql://{user}:{password}@{host}/{database}'
    return url

url = get_url(user, password, host, 'employees')

salaries = pd.read_sql("SELECT * FROM salaries WHERE to_date = '9999-01-01'", url)

salaries.describe()
salaries.salary.mean()
salaries.salary.std()

y = stats.norm(salaries.salary.mean(),salaries.salary.std()).pdf(x)
x = np.arange(salaries.salary.mean()-4*salaries.salary.std(), salaries.salary.mean()+4*salaries.salary.std(), 100)
x = np.arange(0,120000)
plt.plot(x,y)

