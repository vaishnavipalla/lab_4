import math
import numpy as np
import matplotlib.pyplot as plt
p=0.707#input("enter pass band gain")
s=0.01#input("enter stop band gain")
ws=6282#input("enter stop band gain")
wp=3141#input("enter pass band gain")
r=(1/(p*p))-1
q=(1/(s*s))-1
t=np.log(ws/wp)
x=0.5*np.log(r/q)
N=x/t
n=np.around(N)
n=np.abs(n)
print(n)
wc=wp/((r)**(2*n))
print(wc)
H=np.zeros(10000)
for i in range(0,10000):
	k=((i/wc)**(2*n))
	d=np.sqrt(1+k)
	H[i]=1/d
Hmag=np.abs(H)
print(H)
plt.subplot(121)
plt.plot(H)
plt.xlabel("frequency")
plt.ylabel("amplitude")
plt.title ("H")
plt.subplot(122)
plt.plot(Hmag)
plt.title("Hmag")
plt.xlabel("frequency")
plt.ylabel("amplitude")
plt.show()
