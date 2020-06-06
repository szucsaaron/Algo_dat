"""
Author: Aron Abraham Szucs
Matr.Nr.: 11932493
Assigment 4
"""

from My_Maze import My_Maze

my_test_maze = None


def create_maze(maze_type):
    # my_test_maze = My_Maze()

    if maze_type == 0:
        my_test_maze = [[0 for x in range(6)] for y in range(6)]
        my_test_maze[0] = "******"
        my_test_maze[1] = "*    *"
        my_test_maze[2] = "** * *"
        my_test_maze[3] = "*  * *"
        my_test_maze[4] = "* ** *"
        my_test_maze[5] = "**** *"
        return my_test_maze
    else:
        my_test_maze = None
        return my_test_maze


def test_find_exits():
    global my_test_maze
    my_test_maze = My_Maze(create_maze(0))
    start_x, start_y = 1, 1  # define starting point

    # maze before analysis
    print("Maze before analysis: ")
    my_test_maze.dump_maze()  # just for debugging!

    print("\n\nAnalysing maze...")

    # analyse maze
    assert my_test_maze.find_exits(start_x, start_y, 0) == True
    my_test_maze.dump_maze()  # just for debugging!

    # check found exit
    listOfExits = my_test_maze.get_list_of_exits()
    assert 1 == len(listOfExits)
    assert listOfExits[0][0] == 5
    assert listOfExits[0][1] == 4


def test_get_list_of_exits():
    global my_test_maze
    my_test_maze = My_Maze(create_maze(0))
    start_x, start_y = 1, 1  # define starting point

    assert my_test_maze.find_exits(start_x, start_y, 0) == True

    listOfExits = my_test_maze.get_list_of_exits()
    assert 1 == len(listOfExits)
    assert listOfExits[0][0] == 5
    assert listOfExits[0][1] == 4


def test_get_max_recursion_depth():
    global my_test_maze
    my_test_maze = My_Maze(create_maze(0))
    start_x, start_y = 1, 1  # define starting point

    assert my_test_maze.find_exits(start_x, start_y, 0) == True

    assert my_test_maze.get_max_recursion_depth() == 11
