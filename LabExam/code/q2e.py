import numpy as np 

a_0 = 5.29E-11
z_p = 28
A_p = 58
z_t = 30
A_t = 66
rho = 700 #um/cm²
E = 95

a = 0.885*a_0*(z_p**(2/3)+z_t**(2/3))**(-0.5)

alfred = 16256*E/(z_p*z_t*(z_p**(2/3)+z_t**(2/3))**(0.5))

tau = 41.5*rho/((z_p**(2/3)+z_t**(2/3))*A_t)

print(alfred)

print(tau)