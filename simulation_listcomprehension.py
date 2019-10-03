def dice_roll_1():
    return random.choice([1,2,3,4,5,6])

def dice_roll_2():
    return random.choice([1,2,3,4,5,6]) 

sum([dice_roll_1() == dice_roll_2() for i in range(0,n_trials)])/n_trials

Head = 0
Tail = 1

sum([np.random.choice([Head, Tail],8).sum() > 3 for i in range(0,n)])/n

data_science_student = (np.random.random(2) < .25).sum()
data_science_student.sum()

Web_dev = 0
Data_Science = 1

options = [Web_dev]*3 +[Data_Science]*1

sum([(np.random.choice(options, 2)).sum() == 2.0 for i in range(0,10000)])/10000

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