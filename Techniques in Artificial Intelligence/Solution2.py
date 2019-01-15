import sys
import numpy as np


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

    return neighbors_rm(neighbors_range(neighbors_x, neighbors_y), pos)


def neighbors_range(x, y):
    neighbors_list = []
    for i in range(x[0], x[1] + 1):
        for j in range(y[0], y[1] + 1):
            neighbors_list.append([j, i])
    return neighbors_list


def compare_lists(list1, list2):
    n = 0
    for i in list1:
        for j in list2:
            if i == j:
                n = 1
    return n


def neighbors_rm(neighbors_list, pos):
    for n in reversed(neighbors_list):
        if n[0] != pos[0] and n[1] != pos[1]:
            neighbors_list.remove(n)
    neighbors_list.remove(pos)
    return neighbors_list


def allies_rm(neighbors_list, input_matrix):
    for n in reversed(neighbors_list):
        if input_matrix[n[0], n[1]] == 0:
            neighbors_list.remove(n)
    return neighbors_list


def solve_task2(input_matrix):

    # Edit input
    input_matrix[input_matrix == 'X'] = 0
    input_matrix[input_matrix == '.'] = 1
    input_matrix = input_matrix.astype(int)

    # size
    size = np.array([input_matrix.shape[0], input_matrix.shape[1]]) - 1

    enemies_matrix = np.zeros((input_matrix.shape[0], input_matrix.shape[1]))
    neighbors_list = []

    # Get enemies at border
    row, col = np.where(input_matrix == 1)
    for i in range(0, row.shape[0]):
        if row[i] == 0 or row[i] == size[0] or col[i] == 0 or col[i] == size[1]:
            neighbors_list.append([row[i], col[i]])

    neighbors_old = []

    i = -1
    while len(neighbors_list) > i + 1:

        # Get next position from neighbors_list
        i += 1
        pos = neighbors_list[i]

        # Check if new position is in neighbors_old
        pos_old = compare_lists([pos], neighbors_old)

        if pos_old == 0:
            # Append to position to old neighbors
            neighbors_old.append(pos)

            # Get new neighbor positions & add to neighbor list
            neighbors_new = neighbors(pos, size)

            # Remove allies from neighbors
            neighbors_new = allies_rm(neighbors_new, input_matrix)

            # Update enemies at border
            for n in neighbors_new:
                    enemies_matrix[n[0], n[1]] = 1

            neighbors_list = neighbors_list + neighbors_new

    enemies_matrix = enemies_matrix.astype(str)
    enemies_matrix[enemies_matrix == '0.0'] = 'X'
    enemies_matrix[enemies_matrix == '1.0'] = '.'
    enemies_matrix[enemies_matrix == '0'] = 'X'
    enemies_matrix[enemies_matrix == '1'] = '.'

    return enemies_matrix


input_arg = sys.argv[1]


def run_program(filename=input_arg):
    # Read the input matrix
    input_matrix = np.genfromtxt(filename, dtype='str')

    # Your main function to solve the matrix
    output = solve_task2(input_matrix)

    # print the matrix to a txt file
    np.savetxt('output_for_task2.txt', output, fmt="%s")


run_program()
