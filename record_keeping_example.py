import numpy as np

NUMBER_OF_FUNDS = 30
MAX_YR_INVEST = 18000

#random data to test
#vest_id, age, income, balance, contributions, strategy data order
#suppose 30 companies each with 100 employees already ordered
#0-99, 100-199, etc. all belong to the same company
data =  np.genfromtxt('aibcs.csv', delimiter=',', skip_header=1)

#conservative, moderate, aggressive weights
strategy_rates = np.genfromtxt('random_strategy_weights.csv', delimiter=',', skip_header=1)

'''
calculate, for each employee, how much to put into each fund
based on company and individual IRS rules
inputs:
vest_id, need to directly store calculations into database
income this pay period (2 weeks)
total balance in 401(k)
age, which may affects strategy
principal_yr is how much income has been invested this year not including current pay period
strategy is strategy
0 for conservative, 1 for moderate, 2 for aggressive
contribution rate is default to 6%
'''
def calc_employee_contributions(vest_id, income, balance, age, principal_yr = 1000, strategy=0, rate=.06):

    contri_this_period = rate * income

    #IRS rule: no more than 18000 contribution/year
    if contri_this_period + principal_yr >= MAX_YR_INVEST:
        contri_this_period = MAX_YR_INVEST - principal_yr

    contri_fund = contri_this_period * strategy_rates[:,int(strategy)]
    #returns starting bal, ending bal, each fund's contribution this period
    return balance, balance+contri_this_period, contri_fund, contri_this_period

#test example
i = 23
print(calc_employee_contributions(i,data[i,2]/24,data[i,3],data[i,1],strategy=data[i,5],rate=data[i,4]))
