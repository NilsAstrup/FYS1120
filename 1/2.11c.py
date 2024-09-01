import numpy as np
import matplotlib.pyplot as plt

N=21
x=np.linspace(-3,3,N)
y=np.linspace(-3,3,N)

rx,ry=np.meshgrid(x,y,indexing="ij")

a=1
Ex=rx.copy()
Ey=ry.copy()

for i in range(len(rx.flat)):
    Ex.flat[i],Ey.flat[i]=-1/rx.flat[i],1/(ry.flat[i])

Emag=np.sqrt(Ex**2+Ey**2)

nEx=Ex/Emag
nEy=Ey/Emag

plt.quiver(rx, ry, nEx, nEy, np.log10(Emag),cmap="jet")
plt.colorbar()
plt.show()
