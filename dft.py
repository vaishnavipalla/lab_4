from pylab import *
import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
a=int(input("enter number of samples for x[n]:"))
x=[]
print("enter samples:")
for i in range(a):
	y=int(input())
	x=np.append(x,y)
print("x[n]=",x)
N=int(input("enter n points"))
k=4
j=cm.sqrt(-1)
X=[]
w=np.linspace(-np.pi,np.pi,N)
for i in range(0,k):
	sum=0
	for n in range(0,len(x)):
		v=np.exp(-j*2*pi*i*n/N)
		sum=sum+(x[n]*v)
	X.append(sum)
plt.subplot(221)
plt.stem(np.abs(X))
plt.xlabel("frequency(w/pi)")
plt.ylabel("magnitude")
plt.subplot(222)
plt.stem(angle(X)/np.pi)
plt.xlabel("frequency")
plt.ylabel("phase angle in radians")
plt.title("phase spectrum")
plt.show()







