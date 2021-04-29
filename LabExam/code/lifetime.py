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
    x,y,z = np.genfromtxt( filename, unpack=True )
    return x,y,z

c = 2.99798452E2 #um/ps
beta = 0.043
gamma = 1/np.sqrt(1-beta**2)
print(gamma)

x, inten, error = txtreader("lifetime.txt")
time = x/(beta*c)
timer = time/gamma
timefit  = []
intenfit = []
errfit   = []
for i in range(1,len(timer)):
    timefit.append(timer[i])
    intenfit.append(inten[i])
    errfit.append(error[i]*(1/i))
smooth = np.arange(0.5*min(time),1.1*max(time))

k='maroon'

plt.rcParams['font.size'] = 18
expot, experr = curve_fit(expo, timefit, intenfit, sigma=errfit, p0=(1,69))
plt.plot(smooth, expo(smooth, *expot), '--', color='tab:red', label='Exponential fit')

plt.errorbar(timer, inten, yerr=error, fmt='o', color=k, label='Experimental data')
#plt.yscale('log')
plt.grid(which='major', axis='both', linestyle='--', linewidth=1)
plt.ylim(0, 1.1)
plt.ylabel("Normalised Intensity")
plt.xlabel("Time of Flight / ps")
plt.legend()
plt.savefig("lifetime.pdf", bbox_inches = 'tight', pad_inches = 0.1, transparent=True)

for i in range(0,2):
    print(expot[i], "$\pm$", np.sqrt(experr[i][i]))
