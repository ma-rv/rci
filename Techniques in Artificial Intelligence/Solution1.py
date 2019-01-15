import sys
import numpy as np


def update_costs(cost_matrix, n, start, costs_pos):
    if n == start:
        costs = 0
    elif cost_matrix[n[0], n[1]] == 0:
        costs = costs_pos
    elif costs_pos < cost_matrix[n[0], n[1]]:
        costs = costs_pos
    else:
        costs = cost_matrix[n[0], n[1]]

    return costs


def get_costs(n, pos):
    if n[0] == pos[0]:
        costs = 5
    elif n[1] == pos[1]:
        costs = 6
    else:
        costs = 10

    return costs


def neighbors(pos, size):
    if pos[0] == 0:
        neighbors_y = [pos[0], pos[0] + 1]
    elif pos[0] == size[0]:
        neighbors_y = [pos[0] - 1, pos[0]]
    else:
        neighbors_y = [pos[0] - 1, pos[0] + 1]

    if pos[1] == 0:
        neighbors_x = [pos[1], pos[1] + 1]
    elif pos[1] == size[1]:
        neighbors_x = [pos[1] - 1, pos[1]]
    else:
        neighbors_x = [pos[1] - 1, pos[1] + 1]

    return neighbors_range(neighbors_x, neighbors_y)


def neighbors_range(x, y):
    neighbors_list = []
    for i in range(x[0], x[1]+1):
        for j in range(y[0], y[1]+1):
            neighbors_list.append([j, i])
    return neighbors_list


def compare_lists(list1, list2):
    n = 0
    for i in list1:
        for j in list2:
            if i == j:
                n = 1
    return n


def solve_task1(input_matrix):
    quit = False

    # Modify input
    input_matrix[input_matrix == '_'] = 0
    input_matrix[input_matrix == '*'] = 1
    input_matrix[input_matrix == 'R'] = 2
    input_matrix[input_matrix == 'X'] = 3
    input_matrix = input_matrix.astype(int)

    # Get start
    i, j = np.where(input_matrix == 2)
    if i.size!=0 and j.size!=0:
        start = [i[0], j[0]]
    else:
        quit = True  

    # Get goal
    i, j = np.where(input_matrix == 3)
    if i.size!=0 and j.size!=0:
        goal = [i[0], j[0]]
    else:
        quit = True 
    
    if quit==True:
        return'No path found!'
    else:
        # size
        size = np.array([input_matrix.shape[0], input_matrix.shape[1]]) - 1

        # Initialize
        pos = start
        neighbors_list = [pos]
        neighbors_old = []

        # cost_matrix
        cost_matrix = np.zeros(input_matrix.shape)
        row, col = np.where(input_matrix == 1)
        cost_matrix[row, col] = -1

        # neighbors_old
        for i in range(0, row.shape[0]):
            neighbors_old.append([row[i], col[i]])

        i = -1

        # While not reached goal and neighbors left
        while cost_matrix[goal[0], goal[1]] == 0 and len(neighbors_list) > i + 1:

            # Get next position from neighbors_list
            i += 1
            pos = neighbors_list[i]

            # check if new position is in neighbors_old
            pos_old = compare_lists([pos], neighbors_old)

            if pos_old == 0:
                # Append to position to old neighbors
                neighbors_old.append(pos)

                # Get new neighbor positions & add to neighbor list
                neighbors_new = neighbors(pos, size)
                neighbors_new.remove(pos)
                neighbors_list = neighbors_list + neighbors_new

                # Fill cost_matrix at new neighbor positions
                for n in neighbors_new:
                    if cost_matrix[n[0], n[1]] != -1:
                        # calculate costs
                        costs_n = cost_matrix[pos[0], pos[1]] + get_costs(n, pos)

                        # Update costs
                        cost_matrix[n[0], n[1]] = update_costs(cost_matrix, n, start, costs_n)
        # print(i)
        # print(cost_matrix)
        if cost_matrix[goal[0], goal[1]] != 0:
            return int(cost_matrix[goal[0], goal[1]])
        else:
            return'No path found!'


# Get input from command prompt and run the program
input_arg = sys.argv[1]


def run_program(file_name=input_arg):
    # Read the input matrix
    input_matrix = np.genfromtxt(file_name, dtype='str')

    # Your main function to solve the matrix
    print(solve_task1(input_matrix))


run_program()

