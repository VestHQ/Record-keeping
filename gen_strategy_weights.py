import numpy as np

NUMBER_OF_FUNDS = 30

#random weights for now
conservative_weights = np.random.uniform(0,1,NUMBER_OF_FUNDS)
moderate_weights = np.random.uniform(0,1,NUMBER_OF_FUNDS)
aggressive_weights = np.random.uniform(0,1,NUMBER_OF_FUNDS)

c_sum = sum(conservative_weights)
m_sum = sum(moderate_weights)
a_sum = sum(aggressive_weights)

#normalize to sum to 1
conservative_weights /= c_sum
moderate_weights /= m_sum
aggressive_weights /= a_sum

f = open('random_strategy_weights.csv', 'w')
f.write('Conservative,Moderate,Aggressive\n')
for i in range(NUMBER_OF_FUNDS):
    f.write(str(conservative_weights[i])+','+str(moderate_weights[i])+','+str(aggressive_weights[i])+'\n')
f.close()