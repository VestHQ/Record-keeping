import numpy as np
import random

age = []
for i in range(3000):
    age.append(random.randint(24,64))

income = []
for i in range(3000):
    income.append(round(np.random.uniform(25000,150000),2))

balance = []
for i in range(3000):
    balance.append(round(np.random.uniform(0,1000000),2))

contributions = []
for i in range(3000):
    contributions.append(round(np.random.uniform(.01,.1),2))

#0 for conservative, 1 for moderate, 2 for aggressive
cma = []
for i in range(3000):
    cma.append(random.randint(0,2))

f = open('aibcs.csv', 'w')
f.write('Age,Income,Balance,Contributions,Strategy\n')
for i in range(len(income)):
    f.write(str(age[i])+','+str(income[i])+','+str(balance[i])+','+str(contributions[i])+','+str(cma[i])+'\n')
f.close()