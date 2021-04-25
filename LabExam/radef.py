import numpy as np
import scipy
from matplotlib.figure import Figure
from matplotlib.patches import Circle
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def gaussian(x, a, x0, sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))

def expm(x, h, mu, sigma, tau):
    diff = x-mu
    s = sigma**2
    tau = -1*tau

    return (h/(1+((diff*tau)/s)))*np.exp(-0.5/s*diff**2)

def plotSaveGrainHisto(filename):
	#read the file and output the correct count array and plot limits    
    x,y = np.genfromtxt( filename, unpack=True )
    return x,y


x,let =plotSaveGrainHisto("let.txt")

#fill the figure
plt.plot(x,let, color='black')
plt.grid(which='major', axis='both')
plt.xlabel( 'Energy afer substrate [MeV]' )
plt.ylabel( 'LET [MeV/(mg/cm$^2$)]' )
plt.savefig("Kr_let.pdf", bbox_inches = 'tight', pad_inches = 0.1, transparent=True)
plt.show()
#print("Constant= ",popt[0]," +- ", np.diag(pcov)[0], "counts")
#print("Mean= ",popt[1]," +- ", np.diag(pcov)[1], "keV")
#print("Sigma= ",abs(popt[2])," +- ", np.diag(pcov)[2], "keV")
