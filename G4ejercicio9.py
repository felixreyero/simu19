import matplotlib.pyplot as plt

""" a=0.9
k=10
x0=5 """

""" a=0.9
k=10
x0=10 """


a=1.1
k=10
x0=1

def loopx1(x0):
    return (-x0*(a-1)/k + a)*x0

vx=[]
x0=loopx1(x0)
vx.append(x0)
for i in range(1000):
    x0=loopx1(x0)
    vx.append(x0)

print(vx)
plt.scatter(y=vx,x=range(1001)) #usar quiver pyplot
plt.show()