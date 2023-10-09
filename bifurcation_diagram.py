import numpy as np
import matplotlib.pyplot as plt
#logistic map
def logistic(x,k):
    return k*x*(1-x)
#iteration step
k_min = 3 
k_max = 4
t = 0.001
k = np.arange(k_min,k_max,t)
#iteration parameters
m = 10**4
m_drop = 150
K = []
X = []
#figure initialization 
plt.figure(figsize=(8,4),dpi=200)
for i in k:
    x = 0.111
    for j in range(m_drop):
        x = logistic(x,i)
    for j in range(m):
        x = logistic(x,i)
        X.append(x)
        K.append(i)
plt.plot(K,X,"k.", ms=0.01)    
# set diagram parameters
plt.xlim(k_min,k_max) 
plt.ylim(0,1)
plt.xlabel("$k$",fontsize=10)
plt.ylabel("$x$",fontsize=10)
plt.xticks(fontsize=5)
plt.yticks(fontsize=5)  
plt.show()

