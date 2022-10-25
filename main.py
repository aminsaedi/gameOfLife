from time import sleep
from pprint import pprint
import copy

def iteration(donya, w, h):
    new_donya = copy.deepcopy(donya)
    for y in range(h):
        for x in range(w):
            neighbours = 0
            tl = donya[(y-1) % h][(x-1) % w]
            t = donya[(y-1) % h][x]
            tr = donya[(y-1) % h][(x+1) % w]
            r = donya[y][(x+1) % w]
            br = donya[(y+1) % h][(x+1) % w]
            b = donya[(y+1) % h][x]
            bl = donya[(y+1) % h][(x-1) % w]
            l = donya[y][(x-1) % w]
            neighbours = tl + t + tr + r + br + b + bl + l

            if (neighbours < 2):
                new_donya[y][x] = 0
            if (neighbours > 3):
                new_donya[y][x] = 0
            if (donya[y][x] == 0 and neighbours == 3):
                new_donya[y][x] = 1
    return new_donya


w = 29
h = 20
world = [[0 for x in range(w)] for y in range (h)]

# initialzw world
world[1][1] = 2
world[10][10] = 1
world[11][11] = 1
world[12][9] = 1
world[12][10] = 1
world[12][11] = 1

def print_world():
    for ih in range(h):
        for iw in range(w):
            print(world[ih][iw], end=" ")
        print("")
index = 0
while True:
    print_world()
    world = iteration(world, w, h)
    print(f"---------------------------------------------{index}")
    sleep(0.07)
    index+=1
