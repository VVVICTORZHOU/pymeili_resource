# 1. Import the required libraries
import numpy as np
from pymeili import beautifyplot as bp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D

# 2. Create a figure and axis
fig = plt.figure(figsize=(20, 10))
ax1 = bp.initplot(fig.add_subplot(121, projection='3d'), figsize=(10, 10), theme='l')

# 3. Create data for bar3d plot
x = [1, 2, 3, 3.5, 5]
y = 4
z = 1
bp.bar3d(x,y,z,dx=1,dy=1,dz=[1,2,3,4,5]) # dx, dy, dz are the width, depth and height of the bars

# 4. Create data for plot3d and scatter3d plot
x = [1,2,3,4,5]
y = [1,2,3,4,5]
z = [4,5,2,3,5]
bp.plot3d(x, y, z, color='fg3', linestyle='-', linewidth=2.5)
bp.scatter3d(x, y, z, s=100, color='fg3')

# 5. Other plot options
bp.spines(linewidth=5)
bp.xticks([1, 2, 3, 4, 5], [str(i) for i in [1, 2, 3, 4, 5]])
bp.yticks([1, 2, 3, 4, 5], [str(i) for i in [1, 2, 3, 4, 5]])
bp.zticks([1, 2, 3, 4, 5], [str(i) for i in [1, 2, 3, 4, 5]])
bp.xlabel('X')
bp.ylabel('Y')
bp.zlabel('Z')
bp.xlim(0, 6)
bp.ylim(0, 6)
bp.zlim(0, 6)
bp.lefttitle('DEMO 10-1', fontsize=20)

# 6. Create the data for contour3d and contourf3d plot
Nx, Ny, Nz = 100, 300, 500
X, Y, Z = np.meshgrid(np.arange(Nx), np.arange(Ny), np.arange(Nz))
data = (((X+100)**2 + (Y-20)**2 + 2*Z)/1000+1)

# 7. Create the contour3d and contourf3d plot
ax2 = bp.initplot(fig.add_subplot(122, projection='3d'), figsize=(10, 10), theme='l')
bp.plot_surface(X[:,:,0], Y[:,:,0], data[:,:,0], cmap='209')
bp.colorbar(extendrect=False, extendfrac='auto', shrink=0.8, pad=0.05, aspect=15, fraction=0.1, label=f'Colorbar', ticks=np.array([20, 65, 110]), orientation='horizontal',labelsize=20, ticklabelsize=14)



bp.contour3d(X[:,:,0], Y[:,:,0], data[:,:,0], cmap=['#f00000','#00f000','#0000f0','#f0f000','#f000f0'], linewidths=1.5, zdir='z', levels=np.linspace(data.min(), data.max(), 20), offset=0)
bp.contourf3d(X[:,:,0], Y[:,:,0], data[:,:,0], cmap=['#f00000','#00f000','#0000f0','#f0f000','#f000f0'], alpha=0.5, zdir='z', levels=np.linspace(data.min(), data.max(), 20), offset=0)

bp.contour3d(X[0, :, :], data[0, :, :], Z[0, :, :], cmap=['#f00000','#00f000','#0000f0','#f0f000','#f000f0'], linewidths=1.5, zdir='y', levels=np.linspace(data.min(), data.max(), 20), offset=Y.max())
bp.contourf3d(X[0, :, :], data[0, :, :], Z[0, :, :], cmap=['#f00000','#00f000','#0000f0','#f0f000','#f000f0'], alpha=0.5, zdir='y', levels=np.linspace(data.min(), data.max(), 20), offset=Y.max())

bp.contour3d(data[:, -1, :], Y[:, -1, :], Z[:, -1, :], cmap=['#f00000','#00f000','#0000f0','#f0f000','#f000f0'], linewidths=1.5, zdir='x', levels=np.linspace(data.min(), data.max(), 20), offset=0)
bp.contourf3d(data[:, -1, :], Y[:, -1, :], Z[:, -1, :], cmap=['#f00000','#00f000','#0000f0','#f0f000','#f000f0'], alpha=0.5, zdir='x', levels=np.linspace(data.min(), data.max(), 20), offset=0)

# 8. Other plot options
bp.spines()
bp.lefttitle('DEMO 10-2', fontsize=20)
bp.xticks([0, 25, 50, 75, 100], [str(i) for i in [0, 25, 50, 75, 100]])
bp.yticks([0, 100, 200, 300], [str(i) for i in [0, 100, 200, 300]])
bp.zticks([0, 100, 200, 300, 400, 500], [str(i) for i in [0, 100, 200, 300, 400, 500]])
bp.xlabel('X')
bp.ylabel('Y')
bp.zlabel('Z')
bp.xlim(0, 100)
bp.ylim(0, 300)
bp.zlim(0, 500)
bp.set_pane_color(color=False) # Turn off the pane color

# 9. Show the plot
bp.tight_layout()
bp.show()

