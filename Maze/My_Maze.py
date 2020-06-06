"""
Author: Aron Abraham Szucs
Matr.Nr.: 11932493
Assigment 4
"""

class My_Maze:

    def __init__(self, new_maze=None):
        self._maze = new_maze
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.exits = []
        self.depth_counter = 0
        self.states = []
        self.start_x = 0
        self.start_y = 0

    """	 * This method represents the recursive algorithm to find the exits.
	 * The first call of this method shall define the starting point given by
 	 * the parameters start_x and start_y.
	 *
	 * @param start_x defines the x-coordinate of the starting point
	 * @param start_y defines the y-coordinate of the starting point
	 * @param depth represents the currenct recursion depth
	 * @return True is returned if an exit has been found, or false otherwise."""

    def is_exit(self, position):
        if (position[0] == 0 or position[0] == len(self._maze) - 1) or (
                position[1] == 0 or position[1] == len(self._maze) - 1):
            if self._maze[position[0]][position[1]] != "*":
                return True
            else:
                return False
        else:
            return False

    def is_valid_step(self, position):
        if 0 <= position[0] < len(self._maze) and 0 <= position[1] < len(self._maze[0]):
            if self._maze[position[0]][position[1]] == " ":
                return True
            else:
                return False
        else:
            return False

    def find_exits(self, start_x, start_y, depth):
        if self.depth_counter == 0:
            self.start_x = start_x
            self.start_y = start_y
        self.depth_counter += 1
        for move in self.directions:
            new_pos = (start_x + move[0], start_y + move[1])
            if self.is_valid_step(new_pos):
                if self.is_exit(new_pos):
                    self.exits.append(new_pos)
                    return True
                else:
                    if self.is_valid_step(new_pos) and new_pos not in self.states:
                        self.states.append(new_pos)
                    else:
                        continue
            else:
                continue
            if self.find_exits(new_pos[0], new_pos[1], self.depth_counter):
                return True
            else:
                continue
        return False

    """	 * This method returns the list of x-y-coordinates of found exits. The
    * coordinates are stored in a list of tuples [(1st element x, 2nd element y)] and
    *
    * @return list of found exists. If there are no exits the list shall
    * be empty. """

    def get_list_of_exits(self):
        return self.exits

    """  * This method returns the maximum recursion depth after executing find_exits().
    *
    * @return the maximum recursion depth """

    def get_max_recursion_depth(self):
        return self.depth_counter

    """* This method prints the entire maze in the console for debugging."""

    def dump_maze(self):
        processed_maze = [[0 for x in range(6)] for y in range(6)]

        processed_maze[self.start_x][self.start_y] = "S"

        for state in self.states:
            processed_maze[state[0]][state[1]] = "."

        for exit in self.exits:
            processed_maze[exit[0]][exit[1]] = "X"

        for x in range(len(self._maze)):
            for y in range(len(self._maze[x])):
                if processed_maze[x][y] == 0:
                    if self._maze[x][y] == " ":
                        processed_maze[x][y] = " "
                    if self._maze[x][y] == "*":
                        processed_maze[x][y] = "*"

        str_maze = []

        for line in range(len(processed_maze)):
            str_maze.append("".join(processed_maze[line]))

        for line in str_maze:
            print(line)

    """	 *  This method is used to analyse the processed maze after find_exits() has
    *  been executed.
    *
    * @return the maze"""

    # return the maze
    def get_maze(self):
        return self._maze
