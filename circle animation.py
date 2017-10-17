import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

# animation function.  This is called sequentially
def animate(i):
    plt.clf() # Remove this to overlay
    t = np.linspace(0, np.pi * i)
    circ = np.concatenate((np.cos(t), np.sin(t)))
    plt.axis('off')
    plt.plot(np.cos(t), np.sin(t), linewidth=1)
    return

fig = plt.figure()

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, frames=100, interval=1, blit=False)

anim.save('animation.gif', writer='imagemagick', fps=5)

plt.show()