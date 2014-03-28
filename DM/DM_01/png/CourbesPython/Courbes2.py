import matplotlib.pyplot as plt
import numpy as np
from math import sqrt
om0,z = .5,1.5
g=9.81
T1=1/(om0*(z+sqrt(z*z-1)))
T2=1/(om0*(z-sqrt(z*z-1)))


x=np.linspace(0,20,1000)
p1=plt.plot(x,
            (
                1
                +(T1/(T2-T1))*np.exp(-x/T1)
                +(T2/(T1-T2))*np.exp(-x/T2)
                ),label="$\omega_0 = 0,5$, $z=1,5$")

om0,z = 1.,1.5
g=9.81
T1=1/(om0*(z+sqrt(z*z-1)))
T2=1/(om0*(z-sqrt(z*z-1)))

p2=plt.plot(x,
            (
                1
                +(T1/(T2-T1))*np.exp(-x/T1)
                +(T2/(T1-T2))*np.exp(-x/T2)
                ),label="$\omega_0 = 1$, $z=1,5$")

om0,z = 2.,1.5
g=9.81
T1=1/(om0*(z+sqrt(z*z-1)))
T2=1/(om0*(z-sqrt(z*z-1)))

p3=plt.plot(x,
            (
                1
                +(T1/(T2-T1))*np.exp(-x/T1)
                +(T2/(T1-T2))*np.exp(-x/T2)
                ),label="$\omega_0 = 2$, $z=1,5$")

om0,z = 5.,1.5
g=9.81
T1=1/(om0*(z+sqrt(z*z-1)))
T2=1/(om0*(z-sqrt(z*z-1)))

p4=plt.plot(x,
            (
                1
                +(T1/(T2-T1))*np.exp(-x/T1)
                +(T2/(T1-T2))*np.exp(-x/T2)
                ),label="$\omega_0 = 5$, $z=1,5$")

om0,z = 10,1.5
g=9.81
T1=1/(om0*(z+sqrt(z*z-1)))
T2=1/(om0*(z-sqrt(z*z-1)))

p5=plt.plot(x,
            (
                1
                +(T1/(T2-T1))*np.exp(-x/T1)
                +(T2/(T1-T2))*np.exp(-x/T2)
                ),label="$\omega_0 = 10$, $z=1,5$")


plt.grid(True, which="both", linestyle="dotted")
#plt.title("Fonctions trigonometriques")  
#plt.legend([p1, p2], ["Sinus", "Cosinus"])
plt.legend(loc='lower right', fancybox=True, shadow=True, prop=dict(size=10))
plt.xlabel("Temps en $s$")
plt.ylabel("Position $y(t)$ en $m$")
plt.show()


