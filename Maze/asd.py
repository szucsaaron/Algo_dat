# import part
import time
import sys
import os

# global values
load = 0  # set initial loading value
walk = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # set movements
backtracker = []  # set backtracker (remember that this is a stack)
gmainmaze = []  # set initial blank maze


def initialize():  # loading
    sx = 0  # start x value
    sy = 0  # start y value
    ex = 0  # end x value
    ey = 0  # end y value
    while load == 0:  # just some cool animation
        sys.stdout.write("\rloading |")
        time.sleep(0.1)
        sys.stdout.write("\rloading /")
        time.sleep(0.1)
        sys.stdout.write("\rloading -")
        time.sleep(0.1)
        sys.stdout.write("\rloading \\")
        time.sleep(0.1)
        sys.stdout.write("\r")
        mainmaze = loadMaze("maze.txt")  # IMPORTANT: load the maze under the same folder named "maze.txt"
        print("Maze Loaded")
        print(" ")
        time.sleep(1)
        print(" ")
        print("Locating start point...")
        sx, sy = spotter(5, mainmaze)
        time.sleep(1)
        print(" ")
        print("Locating end point...")
        ex, ey = spotter(3, mainmaze)
        print(" ")
        time.sleep(1)
        return sx, sy, ex, ey, mainmaze;
        break
    print(" ")
    sys.stdout.write("\rInitialized!")
    print(" ")
    time.sleep(3)
    os.system("cls")


def loadMaze(filename):
    # load the data from the file into a 2D list
    with open(filename) as i:
        maze = []
        for line in i:
            line = line.strip()
            spawnmaze = line.split(", ")
            maze.append(spawnmaze)
    return maze


def spotter(num, maze):
    # Locate the 'element' in the maze (this can either be "5" or "3")
    num = str(num)
    rowcounter = -1
    linecounter = 0
    for rows in maze:
        rowcounter = rowcounter + 1
        if num in rows:
            for element in rows:
                if element == num:
                    print("Tango Spotted, Grid:", rowcounter, linecounter)
                    return rowcounter, linecounter;
                    break
                linecounter = linecounter + 1


def valid(maze, x, y):  # check if valid
    height = len(maze) - 1
    width = len(maze[0]) - 1
    if 0 <= x <= height and 0 <= y <= width:
        return 1
    else:
        return 0


def solveMaze(sx, sy, ex, ey):  # solve maze
    global gmainmaze
    for i in walk:  # try every direction
        x = sx + i[0]  # make the move
        y = sy + i[1]
        if valid(gmainmaze, x, y):  # check if still in the maze
            if x == ex and y == ey:  # check if reached destination
                print("SITREP:Destination Arrived")
                print("The Logistic Path Is:\n", backtracker)
                print(" ")
                return 1
            else:
                if gmainmaze[x][y] == "0" and (x, y) not in backtracker:  # add to the stack
                    backtracker.append((x, y))
                else:
                    continue
        else:
            continue
        if solveMaze(x, y, ex, ey) == 1:  # Recursion (do the next step)
            return 1
        else:
            continue
    backtracker.pop(-1)  # moveback while
    return 0


def printMaze(maze):
    for x in range(len(maze)):
        for y in range(len(maze[x])):
            print(maze[x][y], end=' ')
        print("")


def visualize(maze):  # a cool function to visualize the maze
    for x in range(len(maze)):
        for y in range(len(maze[x])):
            if maze[x][y] == "5":
                maze[x][y] = "╳"  # path
            elif maze[x][y] == "0":
                maze[x][y] = "░"  # unbeen path
            elif maze[x][y] == "1":
                maze[x][y] = "█"  # wall
            elif maze[x][y] == "3":
                maze[x][y] = "╳"  # basically path as well
            print(maze[x][y], end=' ')
        print("")


def main():
    # initialize the maze
    sx, sy, ex, ey, mainmaze = initialize()
    global gmainmaze
    gmainmaze = mainmaze
    load = 1
    # solve the maze
    gmainmaze[sx][sy] = "0"
    gmainmaze[ex][ey] = "0"  # change the start and end into "0" to make it a way
    solveMaze(sx, sy, ex, ey)
    for i in backtracker:
        gmainmaze[i[0]][i[1]] = "5"
    gmainmaze[sx][sy] = "5"
    gmainmaze[ex][ey] = "3"  # change the start and end back
    # print the maze
    width = len(gmainmaze[0]) - 1
    print("Check Your Map...")
    print("Map:")
    print("--" * (width + 1))
    printMaze(gmainmaze)
    print("--" * (width + 1))
    # visualize the maze uncomment to establish the function (btw check if your terminal can print these unicodes)
    visualize(gmainmaze)
    time.sleep(5)


main()