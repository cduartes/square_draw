import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.image as mpimg
import numpy as np
from random import randint
from matplotlib.path import Path
import math

# NOTE: Another option would be shapely lib

# Create figure and axes
fig,ax = plt.subplots(1)
#grid(b=None, which='major', axis='both', **kwargs)
ax.grid(True, linestyle='dashed')
ax.tick_params(labelcolor='r', labelsize='medium', width=1)

# Plot fixed size
plt.xlim(-10,10)
plt.ylim(-10,10)

# Box to contract
boxes = []
intersections = []
box = patches.Rectangle((-9,-9),18,18,linewidth=1,edgecolor='r', fill = None)
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
f = patches.Rectangle((3,3),2,2,linewidth=1,edgecolor='b', fill = None)
s = patches.Rectangle((4,4),2,2,linewidth=1,edgecolor='g', fill = None)
boxes.append(f)
boxes.append(s)

path_f = Path(f.get_verts())
path_s = Path(s.get_verts())
pc = path_f.intersects_path(path_s, filled = False)
print('path intersection', pc)
min_x = float("inf")
min_y = float("inf")
max_x = float("-inf")
max_y = float("-inf")
if pc:
    for i in range(0,2):
        if f.get_verts()[i][0] < min_x:
            min_x = f.get_verts()[i][0]
        if f.get_verts()[i][0] > max_x:
            max_x = f.get_verts()[i][0]
        if f.get_verts()[i][1] < min_y:
            min_y = f.get_verts()[i][1]
        if f.get_verts()[i][1] > max_y:
            max_y = f.get_verts()[i][1]
    dist_x = abs(max_x-min_x)
    dist_y = abs(max_y-min_y)
    inter = patches.Rectangle((min_x,min_y),dist_x,dist_y,linewidth=1,edgecolor='r', fill = True)
    print(inter.get_verts())
    ax.add_patch(inter)


"""
for (fi,f) in enumerate(boxes):
    for (si,s) in enumerate(boxes):
        pc = f.get_path().intersects_path(s.get_path(), filled = False)
        bbc = f.get_path().intersects_bbox(s.get_bbox(), filled = True)
        print(fi,si,'path intersection', pc , 'bbox intersection',bbc)
"""
for b in boxes:
    ax.add_patch(b)
plt.show()