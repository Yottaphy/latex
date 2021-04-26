import numpy as np
import matplotlib.pyplot as plt

u = 1.6605E-27
MeV = 1.602E-13

m   = 4
M   = 4
k   = 3.184 
K   = 5.486
v2  = 2*k/m
V2  = 2*K/M
q   = 2
Q   = 2
r_E = 4
r_B = 1
R1  = r_E - 0.14/2
R2  = r_E + 0.14/2

e0 = 55726
E0 = 96015

delE = np.arange(-100,100,1)
x = e0 + delE
X = E0 + delE

m0   = 2E-6*q*e0 / (v2*np.log(R2/R1))
print(m0)
M0   = 2E-6*Q*E0 / (V2*np.log(R2/R1))
delm = 2E-6*q*x  / (v2*np.log(R2/R1))
delM = 2E-6*Q*X  / (V2*np.log(R2/R1))

mass = abs(m0 - delm)
Mass = abs(M0 - delM)

plt.plot(delE, mass, label = "$E_0 = 55726\,$V")
plt.plot(delE, Mass, label = "$E_0 = 96015\,$V")
plt.grid(axis="both", which='major')
plt.xlabel("$\Delta E$ [V]")
plt.ylabel("$\delta m$ [u]")
plt.legend()
plt.savefig("massresE.pdf", bbox_inches = 'tight', pad_inches = 0.1, transparent=True)