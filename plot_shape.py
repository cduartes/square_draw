import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from random import randint
from matplotlib.path import Path
import math

def getIntersection(f,s):
    path_f = Path(f.get_verts())
    path_s = Path(s.get_verts())
    pc = path_f.intersects_path(path_s, filled = False)
    #print('path intersection', pc)
    if pc:
        this_boxes = [f,s]
        min_x = min(f.get_verts()[0][0],s.get_verts()[0][0])
        min_y = min(f.get_verts()[0][1],s.get_verts()[0][1])
        max_x = max(f.get_verts()[2][0],s.get_verts()[2][0])
        max_y = max(f.get_verts()[2][1],s.get_verts()[2][1])
        for b in this_boxes:
            min_x = max(min_x,b.get_verts()[0][0])
            min_y = max(min_y,b.get_verts()[0][1])
            max_x = min(max_x,b.get_verts()[2][0])
            max_y = min(max_y,b.get_verts()[2][1])
        dist_x = abs(max_x-min_x)
        dist_y = abs(max_y-min_y)
        inter_box = patches.Rectangle((min_x,min_y),dist_x,dist_y,linewidth=1,fill=True,color='Red')
        #print(inter_box.get_verts())
        return inter_box
    return None

def main():
    # Create figure and axes
    fig,ax = plt.subplots(1)
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

    #TEMP: Should extract the info from contractions in ibex
    for a in range(0,3):
        x_0 = randint(-9,9)
        y_0 = randint(-9,9)
        x_length = randint(1,10)
        y_length = randint(1,10)
        internal_rect = patches.Rectangle((x_0,y_0),x_length,y_length,linewidth=1,edgecolor='b', facecolor='none')
        boxes.append(internal_rect)

    for f in boxes:
        for s in boxes:
            if f != s:
                inter = getIntersection(f,s)
                if inter:
                    ax.add_patch(inter)

    for b in boxes:
        ax.add_patch(b)
    plt.show()

if __name__ == '__main__':
    main()