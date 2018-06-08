import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Rectangle
import numpy as np
from random import randint
from matplotlib.path import Path
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
        inter_box = patches.Rectangle((min_x,min_y),dist_x,dist_y,linewidth=1,fill=True,color='Red')
        return inter_box
    return None

def get_newbox(intersections):
    for i in intersections:
        print(i.get_verts())

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
    """
    rect1 = patches.Rectangle((2,2),5,2,linewidth=1,fill=False)
    rect2 = patches.Rectangle((5,1),2,4,linewidth=1,fill=False)
    rect3 = patches.Rectangle((1,1),5,3,linewidth=1,fill=False)
    this_boxes.append(rect1)
    this_boxes.append(rect2)
    this_boxes.append(rect3)
    """
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
    intersections = []
    # Add the patch to the Axes
    ax.add_patch(box)
    for f in boxes:
        for s in boxes:
            if f != s:
                intersection = intersect(f,s)
                
                if intersection:
                    intersections.append(intersect(f,s))
                    print(intersection.get_verts())
                    min_x = min(min_x,intersection.get_verts()[0][0])
                    min_y = min(min_y,intersection.get_verts()[0][1])
                    max_x = max(max_x,intersection.get_verts()[2][0])
                    max_y = max(max_y,intersection.get_verts()[2][1])
                    ax.add_patch(intersection)
    # Show patches in plot.
    dist_x = abs(max_x-min_x)
    dist_y = abs(max_y-min_y)
    new_box = patches.Rectangle((min_x,min_y),dist_x,dist_y,linewidth=2,linestyle='dashed',fill=None, color="g")
    print(new_box.get_verts())
    ax.add_patch(new_box)

    print(intersections[0].get_verts())
    #new_box2 = get_newbox(intersections)

    for b in boxes:
        ax.add_patch(b)
    plt.show()

if __name__ == '__main__':
    main()