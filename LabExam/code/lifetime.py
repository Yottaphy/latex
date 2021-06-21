import numpy as np
import scipy as sc
from matplotlib.figure import Figure
from matplotlib.patches import Circle
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#functions defined for exponential decay (expo) and double exponential (expo2)
def expo(t, N_0, tau):
    return N_0*(np.exp(-t/tau))
def expo2(t, N_0, N_1, N_2, tau1, tau2):
    return N_0*expo(t, N_1, tau1)*expo(t, N_2, t-tau2)


#read the file and output the correct count array and plot limits    
def txtreader(filename):
    x,y,z = np.genfromtxt( filename, unpack=True )
    return x,y,z

#relevant constants
c = 2.99798452E2 #um/ps
beta = 0.043
gamma = 1/np.sqrt(1-beta**2)
print(gamma)

#read 3 columns in order
x, inten, error = txtreader("lifetime.txt")
time = x/(beta*c)
timer = time/gamma

#define arrays for the fit curve
timefit  = []
intenfit = []
errfit   = []
for i in range(1,len(timer)):
    timefit.append(timer[i])
    intenfit.append(inten[i])
    errfit.append(error[i]*(1/i))

#make a smooth array of times for the plot
smooth = np.arange(0.5*min(time),1.1*max(time))

#define some nicer format for the plots
k='maroon'
plt.rcParams['font.size'] = 18


#FITTING FUNCTION: fit with expo, xvalues=timefit, yvalues=intenfit, error=errfit, p0 is the initial values for N_0 and tau, respectively.

#expot, experr are the matrix elements giving you the fit parameters and their uncertainty, respectively
expot, experr = curve_fit(expo, timefit, intenfit, sigma=errfit, p0=(1,69))

#plot the values of the fit with smooth in the x axis as a dotted line. The * outputs the whole vector expot instead of just one element.
plt.plot(smooth, expo(smooth, *expot), '--', color='tab:red', label='Exponential fit')

#plot the experimental data (from the text file) as dots with error bars. 
plt.errorbar(timer, inten, yerr=error, fmt='o', color=k, label='Experimental data')

#more format for the plots
#plt.yscale('log')
plt.grid(which='major', axis='both', linestyle='--', linewidth=1)
#plt.ylim(0, 1.1)
plt.ylabel("Normalised Intensity")
plt.xlabel("Time of Flight / ps")
# plt.yscale("log")
plt.legend()

#save plot as a pdf (vector images are superior, change my mind) with transparency
plt.savefig("lifetime2.pdf", bbox_inches = 'tight', pad_inches = 0.1, transparent=True)

#print the fit parameters and errors.
for i in range(0,2):
    print(expot[i], "$\pm$", np.sqrt(experr[i][i]))
