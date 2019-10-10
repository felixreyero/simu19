import matplotlib.pyplot as plt

a=-0.5
b=0.1
c=-3
d=-0.8

x0=1
y0=1

def loop(x0,y0):
    x=a*x0+b*y0
    y=c*x0+d*y0
    return x,y

vx=[]
vy=[]
x0,y0=loop(x0,y0)
vx.append(x0)
vy.append(y0)
for i in range(1000):
    x0,y0=loop(x0,y0)
    vx.append(x0)
    vy.append(y0)

print(vx,vy)
plt.scatter(x=vx,y=vy) #usar quiver pyplot
#plt.quiver(vx,vy,)
plt.show()