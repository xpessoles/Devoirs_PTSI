import matplotlib.pyplot as plt
import numpy as np
from math import sqrt
from math import asin
om0,z = .5,0.5
g=9.81



x=np.linspace(0,20,1000)
p1=plt.plot(x,
            (
                1
                -(1/sqrt(1-z*z))*np.exp(-z*om0*x)
                *np.sin(om0*sqrt(1-z*z)*x+asin(sqrt(1-z*z)))
                ),label="$\omega_0 = 0,5$, $z=0,5$")

om0,z = 1.,0.5

p2=plt.plot(x,
            (
                1
                -(1/sqrt(1-z*z))*np.exp(-z*om0*x)
                *np.sin(om0*sqrt(1-z*z)*x+asin(sqrt(1-z*z)))
                ),label="$\omega_0 = 1$, $z=0,5$")

om0,z = 2.,0.5

p3=plt.plot(x,
            (
                1
                -(1/sqrt(1-z*z))*np.exp(-z*om0*x)
                *np.sin(om0*sqrt(1-z*z)*x+asin(sqrt(1-z*z)))
                ),label="$\omega_0 = 2$, $z=0,5$")

om0,z = 5.,0.5

p4=plt.plot(x,
            (
                1
                -(1/sqrt(1-z*z))*np.exp(-z*om0*x)
                *np.sin(om0*sqrt(1-z*z)*x+asin(sqrt(1-z*z)))
                ),label="$\omega_0 = 5$, $z=0,5$")

om0,z = 10,0.5

p5=plt.plot(x,
            (
                1
                -(1/sqrt(1-z*z))*np.exp(-z*om0*x)
                *np.sin(om0*sqrt(1-z*z)*x+asin(sqrt(1-z*z)))
                ),label="$\omega_0 = 10$, $z=0,5$")


plt.grid(True, which="both", linestyle="dotted")
#plt.title("Fonctions trigonometriques")  
#plt.legend([p1, p2], ["Sinus", "Cosinus"])
plt.legend(loc='lower right', fancybox=True, shadow=True, prop=dict(size=10))
plt.xlabel("Temps en $s$")
plt.ylabel("Position $y(t)$ en $m$")
plt.show()


