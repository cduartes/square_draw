import matplotlib.patches as patches
from matplotlib.path import Path
import matplotlib.pyplot as plt
from random import randint
import numpy as np
import math

def intersect(f,s):
    '''
    Return a new patches.Rectangle with the intersection between two patches.Rectangle (f and s parameters) there's one.
    '''
    path_f = Path(f.get_verts())
    path_s = Path(s.get_verts())
    pc = path_f.intersects_path(path_s, filled = False)
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
        inter_box = patches.Rectangle((min_x,min_y),dist_x,dist_y,linewidth=1,fill=True,color='r')
        return inter_box
    return None

# TODO
def read_data():
    '''
    Reads data on file and returns a single patches.Rectangle as main box and a collection of patches.Rectangle's 
    '''
    # Box to contract
    box = patches.Rectangle((-9,-9),18,18,linewidth=1,fill = None,color='r')
    this_boxes = []

    # TEMP: Should extract the info from contractions in ibex
    for a in range(0,8):
        x_0 = randint(-9,1)
        y_0 = randint(-9,1)
        x_length = randint(1,6)
        y_length = randint(1,6)
        internal_rect = patches.Rectangle((x_0,y_0),x_length,y_length,linewidth=1,fill=False, color="b")
        this_boxes.append(internal_rect)
    return box,this_boxes

def main():
    min_x = float("inf")
    min_y = float("inf")
    max_x = float("-inf")
    max_y = float("-inf")
    
    # Create figure and axes
    fig,ax = plt.subplots(1)
    ax.grid(True, linestyle='dashed')
    ax.tick_params(labelcolor='r', labelsize='medium', width=1)
    # Fix size
    plt.xlim(-10,10)
    plt.ylim(-10,10)

    box,boxes = read_data()
    # Add the patch to the Axes
    ax.add_patch(box)
    for f in boxes:
        for s in boxes:
            if f != s:
                this_intersection = intersect(f,s)
                if this_intersection:
                    min_x = min(min_x,this_intersection.get_verts()[0][0])
                    min_y = min(min_y,this_intersection.get_verts()[0][1])
                    max_x = max(max_x,this_intersection.get_verts()[2][0])
                    max_y = max(max_y,this_intersection.get_verts()[2][1])
                    ax.add_patch(this_intersection)
    # Show patches in plot.
    dist_x = abs(max_x-min_x)
    dist_y = abs(max_y-min_y)
    new_box = patches.Rectangle((min_x,min_y),dist_x,dist_y,linewidth=2,linestyle='dashed',fill=None, color="r")
    if new_box:
        ax.add_patch(new_box)
    for b in boxes:
        ax.add_patch(b)
    plt.show()

if __name__ == '__main__':
    main()