import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.image as mpimg
import numpy as np
from random import randint
from matplotlib.path import Path

# NOTE: Another option would be shapely lib

# Create figure and axes
fig,ax = plt.subplots(1)
#grid(b=None, which='major', axis='both', **kwargs)
ax.grid(True, linestyle='dashed')
ax.tick_params(labelcolor='r', labelsize='medium', width=1)

# Plot fixed size
plt.xlim(-10,10)
plt.ylim(-10,10)

"""
# Display some image
img = mpimg.imread('stinkbug.png')
imgplot = plt.imshow(img)
"""
"""
# Display some functions
t = np.arange(0.0, 2.0, 0.01)
s = np.sin(2 * np.pi * t)
# Add functions to plot
ax.plot(t,s)
"""

# Box to contract
boxes = []
box = patches.Rectangle((-9,-9),18,18,linewidth=1,edgecolor='r',facecolor='none')
# Add the patch to the Axes
ax.add_patch(box)

"""
#TEMP: Should extract the info from contractions in ibex
for a in range(0,2):
    x_0 = randint(-9,9)
    y_0 = randint(-9,9)
    x_length = randint(1,10)
    y_length = randint(1,10)
    internal_rect = patches.Rectangle((x_0,y_0),x_length,y_length,linewidth=1,edgecolor='b', facecolor='none')
    boxes.append(internal_rect)
"""
f = patches.Rectangle((3,3),1,1,linewidth=1,edgecolor='b', fill = None)
s = patches.Rectangle((4,4),1,1,linewidth=1,edgecolor='y', fill = None)
boxes.append(f)
boxes.append(s)


path_f = Path(f.get_verts())
path_s = Path(s.get_verts())

pc = path_f.intersects_path(path_s, filled = True)
bbc = path_f.intersects_bbox(s.get_bbox(), filled = True)
print('path intersection', pc , 'bbox intersection',bbc)

"""
for (fi,f) in enumerate(boxes):
    for (si,s) in enumerate(boxes):
        pc = f.get_path().intersects_path(s.get_path(), filled = False)
        bbc = f.get_path().intersects_bbox(s.get_bbox(), filled = True)
        print(fi,si,'path intersection', pc , 'bbox intersection',bbc)
"""
for p in boxes:
    ax.add_patch(p)
plt.show()