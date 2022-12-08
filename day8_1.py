
import numpy as np

input_file = open('input/input_day8_1.txt', 'r')
# input_file = open('input/input_test.txt', 'r')

tree_heights = np.array([[int(i) for i in line.strip()] for line in input_file], dtype=object)
visible_dict = dict([((i, j), False) for i in range(tree_heights.shape[0]) for j in range(tree_heights.shape[1])])


def search_trees(tree_heights, direction):
    tree_array = tree_heights.copy()
    i_range = range(tree_array.shape[0]) if direction[1] == 1 else range(tree_array.shape[0])[::-1]
    j_range = range(tree_array.shape[1]) if direction[1] == 1 else range(tree_array.shape[1])[::-1]

    for i in i_range:
        for j in j_range:
            if tree_array[i][j] >= 0:
                visible_dict[(i, j)] = True
                if direction[0] == 'row':
                    tree_array[i, :] = tree_array[i, :] - tree_array[i][j] - 1
                else:
                    tree_array[:, j] = tree_array[:, j] - tree_array[i][j] - 1


for dim in ['row', 'col']:
    for rev in [-1, 1]:
        search_trees(tree_heights, (dim, rev))

print(sum(visible_dict.values()))




