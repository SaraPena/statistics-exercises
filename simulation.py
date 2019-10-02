# How likely is it that you roll doubles when rolling two dice?
import numpy as np 
import pandas as pd 
import math

np.random.seed(3)

# Write a two dimensional matrix. Create a matrix where each row represents one "trial". Each row will have two columns, representing 2 dice rolls.

dice_sides = 6

n_trials = nrows = 10000000

n_dice = ncols = 2

dice_numbers = list(range(1,dice_sides + 1))

rolls = np.random.choice(dice_numbers, (nrows,ncols))

rolls = pd.DataFrame(rolls)

doubles = rolls[rolls[1] == rolls[0]]

count_doubles = len(doubles)

p_doubles = count_doubles/n_trials


# If you flip 8 coins, what is the probability of getting exactly 3 heads?
# What is the probability of getting more than 2 heads?

Head = 1

Tail = 0

coin_sides = [Head, Tail]

n_trials = nrows = 10000

n_coins = ncols = 8


coin_flips = np.random.choice(coin_sides, (nrows,ncols))

sums_by_trial = coin_flips.sum(axis = 1)

#Creating a boolean array of True/False for the sum of 8 coin flips exactly equal to 3 heads

exactly_three = sums_by_trial == 3

# We can manipulate the boolean array as 1's and 0's.
# If we take the mean of the array it will give us the rate of success, because it is only summing up the successes (True = 1, False = 0) and dividing the by the number of trials.

exactly_three_rate = exactly_three.mean()

# There are approximately 3 web development cohorts for every 1 datascience cohort at Codeup. 
# Assuming that Codeup randomly selects an Alumni to put on a billboard, what are the odds that the two billboards I drive past both have data science students on them?

p_Web_dev = .75 

p_Data_Science = .25

n_trials = nrows = 100000

n_billboards = 2

# To determine whether or not a student on the billboard is a Data Science student we'll generate a random number between 0 and 1, and say that it is a Data Science student if it is less than our probability of it Being a Data Science student.

data = np.random.random((nrows,n_billboards))

data_science_student = data < p_Data_Science

(data_science_student.sum(axis = 1) == 2).mean()

# Codeup students buy, on average, 3 poptart packages (+- 1.5) a day from the snack vending machine.
# If on Monday the machine resocked with 17 poptart packages, how likely is it that I will be able to buy some poptarts on Friday afternoon?

n_poptart_packages = 17

n_days = 5

n_simulations = nrows = 10000

poptart_packages = np.round(np.random.normal(3, 1.5, (nrows,n_days)))

pt_consumption = np.where(poptart_packages < 0, 0, poptart_packages)

sum_poptart_packages = pt_consumption.sum(axis = 1)

friday_poptarts = sum_poptart_packages < 17

friday_poptarts_rate = friday_poptarts.mean()


## Pandas Solution:
s = pd.Series([1, 2, 3, -1, 4])
# Pandas returns 0 of the condition is "True"
s.where(s > 0,0)


# 5. Compare Heights:
    # Men have an average height of 178 cm and standard deviation of 8cm.
    # Women have a mean of 170, sd = 6cm
    # If a man and woman are chosen at random, P(woman taller than man)?

Man_height =np.random.normal(178, 8, 10000)

Woman_height = np.random.normal(170, 6, 10000)

heights = pd.DataFrame({'M': Man_height, 'W': Woman_height})

height_difference = heights['W'] - heights['M']

Woman_taller = height_difference > 0

Woman_taller_rate = Woman_taller.mean()

# 6. When installing anaconda on a student's computer, there's a 1 in 250 chance that the download is corrupted, and the installation fails.
#    What are the odds that after having 50 students download anaconda, no one has an installation issue? 100 students?

p_installation_fail = 1/250

n_installations = ncols = 150

n_simulations = nrows = 10000


data = np.random.random((nrows, ncols))

install_fail = data < p_installation_fail

sum_of_corrupt_downloads = install_fail.sum(axis = 1) > 0

install_fail_rate = sum_of_corrupt_downloads.mean()


#    100 students success?

n_installations = nrows = 100

data = np.random.random(n_installations)

install_success = data > p_installation_fail

install_success_rate = install_success.mean()

#    What is the probability that we observe an installation issue within the first 150 students that download anaconda?

n_installations = nrows = 150

data = np.random.random(n_installations)

install_fail = data < p_installation_fail

install_failure_rate = install_fail.mean()

#    How likely is it that 450 students all download anaconda with an issue?

n_installations = nrows = 450

data = np.random.random(n_installations)

install_success = data > p_installation_fail

install_success_rate = install_success.mean()

# 7. There's a 70% chance on any given day that there will be at least one food truck at Travis Park. However, you haven't seen a food truck there in 3 days. How unlikely is this?

p_food_truck = .7

p_no_food_truck = 1 - p_food_truck

ndays = ncols = 3

n_simulated_weeks = nrows = 10000

data = np.random.choice(['Food Truck', 'No Food Truck'], 20, p=[p_food_truck, p_no_food_truck])

food_truck = (data == 'Food Truck')

food_truck_rate = food_truck.mean()

# How likely is it that a food truck will show up sometime this week?

ndays = ncols = 7

n_simulated_weeks = nrows = 10000

data = np.random.random((nrows,ncols))

food_truck = data < p_food_truck

food_truck_rate = food_truck.mean()

# If 23 people are in the same room, what are the odds that two of them share a birthday? What if it's 20 people? 40?

people = 23

data = pd.DataFrame(np.random.choice(list(range(1,366)),(100000,people)))
data.nunique(axis = 1)
(data.nunique(axis = 1) != people).mean()

people = 29

data = pd.DataFrame(np.random.choice(list(range(1,366)),(10000,people)))
data.nunique(axis = 1)
(data.nunique(axis = 1) != people).mean()

people = 20


def birthday_match(people):
    """
    Create function that will return the probability of two people in a room having the same birthday. variable people = # of people in the group.
    """
    data = pd.DataFrame(np.random.choice(list(range(1,366)),(10000,people)))
    data.nunique(axis = 1)
    return (data.nunique(axis = 1) != people).mean()

birthday_match(23)
birthday_match(29)
birthday_match(20)
birthday_match(40)





