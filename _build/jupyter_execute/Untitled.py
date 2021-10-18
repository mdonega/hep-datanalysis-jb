import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

# multivariate gaussian mu = 0; sigma = 1
def gg(x, y):
    return 1./(2*math.pi) * np.exp(-0.5*(x*x +y*y))

# gaussian mu = 1; sigma 
# def g(x, sigma):
#     return 1./math.sqrt(2*math.pi)/sigma * np.exp(-0.5*(x*x))

x = np.linspace(-5, 5, 1000)
y = np.linspace(-5, 5, 1000)
X, Y = np.meshgrid(x, y)
G = gg(X, Y)

fig = plt.figure(figsize=(6, 6))
ax1 = plt.axes(projection='3d')
ax1.plot_surface(X, Y, G,cmap='Greys', linewidth=0)
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')

# Conditional distribution
# p(X=x, y=1)
xline = x
yline = -1.+0.*y
zline = gg(xline,yline)

ax1.plot3D(xline, yline, zline, 'red', label='p(X=x,Y)',linewidth=3.0)


fig = plt.figure(figsize=(6, 6))
ax2 = fig.gca(projection='3d')
#ax1 = plt.axes(projection='3d')
ax2.plot_surface(X, Y, G, cmap='Greys')
cset = ax2.contourf(X, Y, G, zdir='x', offset=-5, cmap='Greys')
cset = ax2.contourf(X, Y, G, zdir='y', offset=5, cmap='Greys')
ax2.set_xlim(-5, 5)
ax2.set_ylim(-5, 5)
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')

plt.show()



import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal

x = np.linspace(-5,5,100)
y = np.linspace(-5,5,100)
X, Y = np.meshgrid(x,y)
pos = np.empty(X.shape + (2,))
pos[:, :, 0] = X 
pos[:, :, 1] = Y

mean = np.array([0, 0])
cov  = np.array([[1,0],[0,1]])
xy = multivariate_normal(mean,cov)

# Make a 3D plot
fig = plt.figure(figsize=(6, 6))
ax = fig.gca(projection='3d')
ax.plot_surface(X, Y, xy.pdf(pos),cmap='turbo',linewidth=0)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
