import matplotlib.pyplot as plt
import numpy as np
n=input("enter x length:")
x=[]
y=[]
l=np.arange(0,n,1)
for i in range(n):
	a=input("enter the elements:")
	x.append(a)
print(x)
for i in range(n):
	z=x[(n-1-i)]
	y.append(z)
print(y)
#s=0
#m=[]
#for i in range(n+n-1):
	#for j in range(n):
		#s=s+((x[j]*(y[i-j]))
	#m.append(s)
	#s=0
#print(m)
#plt.subplot(3,1,1)
#plt.stem(l,x)
#plt.subplot(3,1,2)
#plt.stem(l,y)
#plt.subplot(3,1,3)
#plt.stem(l,m)
#plt.show()
