import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.colors import ListedColormap
#logistic map
def logistic(x,k):
    return k*x*(1-x)
#Number of intervals and bars
B = 1000
S_low = 0
S_up = 1
b_mid = np.arange(S_low + (S_up-S_low)/(2*B), S_up, (S_up-S_low)/B)
#iteration step
k_min = 3 
k_max = 4
t = 0.001
k = np.arange(k_min,k_max,t)
#iteration parameters
m = 10**4
m_drop = 150
#figure initialization 
plt.figure(figsize=(8,4),dpi=200)
#set colormap 
cmap = mpl.colormaps["viridis"]
newcolors = cmap(np.linspace(0, 1, 256))
newcolors[:1, :] = np.array([0, 0, 0, 1])
newcmap = ListedColormap(newcolors)
F = (5/B)
norm = mpl.colors.Normalize(vmin=0, vmax=F)
for i in k:
    x = 0.111
    X = []
    for j in range(m_drop):
        x = logistic(x,i)
    for j in range(m):
        x = logistic(x,i)
        X.append(x)
    #compute frequency for each interval    
    hist = np.histogram(X,bins=B,range=(S_low,S_up))[0]    
    freq = [min(j,F) for j in hist/m]
    #plot the diagram
    plt.scatter(np.full((1,B),i),b_mid,s=0.1,c=freq,norm=norm,cmap=newcmap,marker=".")
# set diagram parameters
plt.xlim(k_min,k_max) 
plt.ylim(S_low,S_up)
plt.xlabel("$k$",fontsize=10)
plt.ylabel("$x$",fontsize=10)
plt.xticks(fontsize=5)
plt.yticks(fontsize=5)
#set colorbar parameters    
cbar = plt.colorbar(ticks=[i/1000 for i in range(6)])
cbar.set_ticklabels([i/10 for i in range(5)]+[r"$\geqslant 0.5\%$"])
cbar.ax.tick_params(labelsize=5)    
plt.show()