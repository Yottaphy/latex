import numpy as np
import scipy as sc
from matplotlib.figure import Figure
from matplotlib.patches import Circle
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def expo(t, N_0, tau):
    return N_0*(np.exp(-t/tau))
def expo2(t, N_0, N_1, N_2, tau1, tau2):
    return N_0*expo(t, N_1, tau1)*expo(t, N_2, t-tau2)
def txtreader(filename):
	#read the file and output the correct count array and plot limits    
    x,y = np.genfromtxt( filename, unpack=True )
    return x,y

x, y = txtreader("ddcm.txt")
a, b = txtreader("ddcm2.txt")
z1 =[]
z2 =[]
diff = []
d1 = []
for i in range(0,len(x)):
    if (x[i-1] > 4E-11) and (x[i] < 1E-10): 
        d1.append((-y[i-1]+y[i])/(x[i]-x[i-1]))
        z1.append(y[i])
d2 = []
for i in range(0,len(a)):
    if (a[i-1] > 4E-11) and (a[i] < 1E-10): 
        d2.append((-b[i-1]+b[i])/(a[i]-a[i-1]))
        z2.append(b[i])

for i in range(0,len(z1)):  
    diff.append(-z1[i]+z2[i])

xz = np.arange(4E-11, 1E-10, (1E-10-4E-11)/len(diff))
avg1 = sum(d1) / len(d1)
avgdiff = sum(diff) / len(diff)
tau = -0.3/avg1
errtau = tau*np.sqrt(len(d1))/len(d1)
print(tau/1E-12, "ps", errtau/1E-12)


plt.rcParams['font.size'] = 18

plt.plot(x, y, '-',  color="green", label='State i')
plt.plot(a, b, '-',  color="red", label='Feeder')
plt.axvline(x=4E-11, linestyle='--', color="black")
plt.axvline(x=1E-10, linestyle='--', color="black")
#plt.yscale('log')
plt.grid(which='both', axis='both', linestyle='dotted', linewidth=1)
plt.ylabel("Intensity")
plt.xlabel("Time / s")
plt.xscale("log")
plt.legend()
plt.savefig("ddcm.pdf", bbox_inches = 'tight', pad_inches = 0.1, transparent=True)

