import numpy as np
import scipy.stats as stats

# How likely is it that you roll doubles when rolling two dice?
n_trials = 2 # rolling two dice
n_simulations = 10,000 # each row will be a simulation

# Create rolls and simulations
rolls = np.random.choice([1,2,3,4,5,6],(10000,2)) 

# Check for doubles, and take the mean of True, False (0,1) to calculate the rate of rolling doubles

doubles_rate= (rolls[:,0] == rolls[:,1]).mean()

# List comprehension technique

def dice_roll_1():
    return random.choice([1,2,3,4,5,6])

def dice_roll_2():
    return random.choice([1,2,3,4,5,6]) 

sum([dice_roll_1() == dice_roll_2() for i in range(0,n_trials)])/n_trials

# rvs() technique

die_distribution = stats.randint(1,7).rvs((10000,2))

doubles = die_distribution[:,0] == die_distribution[:,1]
doubles.mean()

# Probability Distribution technique

# Probability that you roll any number : 1/6
# Each number on 2 indepedent dice have a 1/6 change of being rolled. 1/6 + 1/6 

roll_dice_distribution = (stats.randint(1,7).pmf(3) + stats.randint(1,7).pmf(3))

stats.binom(1,6/36).pmf(1)
# Doubles on a dice can only be rolled 6 ways out of 12 possible sums : 2,4,6,8,10,12 or 6/12 or .50
# Finding the probability of doubles we can take our rolls_distribution, and multiply it my the binomial of .50  probability of success

# 2. If you flip 8 coins, what is the probability of getting exactly 3 tails?
# What is the probability of getting 3 or more tails?

# Create simulations
tosses = np.random.choice(['Heads','Tails'],(10000,8))

#Sum across rows where 'Tails' is true. Find sums == 3, and take the mean of the list.
((tosses == 'Tails').sum(axis = 1) == 3).mean()

# 3 or more tails?
((tosses == 'Tails').sum(axis = 1) > 3).mean()

# List comprehension technique:

Head = 0
Tail = 1

sum([np.random.choice([Head, Tail],8).sum() > 3 for i in range(0,n_trials)])/n_trials

#Probability Distribution

stats.binom(8,.5).pmf(3)

# 3. There are approximately 3 web development cohorts for every 1 data science cohort at Codeup.
#    Assuming that Codeup randomly selects an alumni to put on a billboard, what are the odds taht two billboards I drive past both have data science students on them?

# Create simulations

students = np.random.choice(['Web Dev', 'Web Dev', 'Web Dev', 'Data Science'],(10000,2))
((students == 'Data Science').sum(axis =1) == 2).mean()

# List Comprehension Technique

Web_dev = 0
Data_Science = 1

options = [Web_dev]*3 +[Data_Science]*1

sum([(np.random.choice(options, 2)).sum() == 2.0 for i in range(0,10000)])/10000

# Probability Distribution

stats.binom(2,.25).pmf(2)

# 4. Codeup students buy, on average, 3 poptart packages(+- 1.5) a day from the snack vending machine.
#    If on monday the machine is restocked with 17 poptart packages, how likely is it that I will be able to buy some poptarts on Friday afternoon?

mean = 3
std = 1.5
days = 5

week_poptart_consumption = np.round(np.random.normal(3,1.5,(10000,5)))
week_poptart_consumption = np.where(week_poptart_consumption < 0, 0, week_poptart_consumption)

(week_poptart_consumption.sum(axis = 1) < 17).mean()

# List Comprehension Technique

def consumption(mean,std,days):
    pt_consumption = np.round(np.random.normal(mean,std,days))
    pt_consumption = np.where(pt_consumption < 0, 0, pt_consumption)
    return np.int_(pt_consumption.sum())

sum([consumption(3,1.5,5) < 17 for i in range(0,10000)])/10000

# Probability Distribution

1.5*5

stats.norm(3,1.5).cdf(4)**5

def m_height(mean, std):
    return np.random.normal(mean, std)

def f_height(mean,std):
    return np.random.normal(mean, std)

sum([m_height(178, 8) < f_height(170,6) for i in range(0,10000)])/10000

p_corruption = 1/250

sum([(np.random.random(50) < p_corruption).sum() == 0 for i in range(0,n)])/n
sum([(np.random.random(100) < p_corruption).sum() == 0 for i in range(1,n)])/n


sum([(np.random.random(150) < p_corruption).sum() > 0 for i in range(0,n)])/n

p_Food_Truck = .7
p_No_Food_Truck = .3

sum([(np.random.random(3) < p_Food_Truck).sum() == 0 for i in range(0,10000)])/10000

sum([(np.random.random(7) < p_Food_Truck).sum() > 0 for i in range(0,10000)])/10000

def birthdays(p):
    birthdays = np.random.choice(range(365),p)
    return pd.Series(birthdays).nunique()

sum([birthdays(23) < 23 for i in range(0,n)])/n
sum([birthdays(40) < 40 for i in range(0,n)])/n
sum([birthdays(29) < 29 for i in range(0,10000)])/10000