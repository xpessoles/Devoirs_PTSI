import matplotlib.pyplot as plt
import numpy as np
from math import acos
from math import sqrt
K=1.05
z=0.3
om0=3.


x=np.linspace(0,10,1000)
p1=plt.plot(x,
            (
                K*(1-(np.exp(-z*om0*x)/(sqrt(1-z*z)))*np.sin(om0*x*sqrt(1-z*z)+acos(z)) )  
                ),label="$s(t)$")
p2=plt.plot(x,
            (
                1+x*0
                ),label="$e(t)$")


plt.grid(True, which="both", linestyle="dotted")
#plt.title("Fonctions trigonometriques")  
#plt.legend([p1, p2], ["Sinus", "Cosinus"])
plt.legend(loc='lower right', fancybox=True, shadow=True, prop=dict(size=10))
plt.xlabel("Temps en $s$")
#plt.ylabel("Position $y(t)$ en $m$")
plt.show()


