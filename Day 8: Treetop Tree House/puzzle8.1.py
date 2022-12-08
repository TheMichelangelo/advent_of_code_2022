def tree_is_visible(forest: list, position_x: int, position_y: int) -> bool:
    isVisible = True
    search_x_pos = 0
    current_tree = forest[position_x][position_y]
    while isVisible and search_x_pos < position_x:
        isVisible = forest[search_x_pos][position_y] < current_tree
        search_x_pos += 1
    if isVisible:
        return True

    isVisible = True
    search_x_pos = len(forest[position_x]) - 1
    while isVisible and search_x_pos > position_x:
        isVisible = forest[search_x_pos][position_y] < current_tree
        search_x_pos -= 1
    if isVisible:
        return True

    isVisible = True
    seatch_y_pos = 0
    while isVisible and seatch_y_pos < position_y:
        isVisible = forest[position_x][seatch_y_pos] < current_tree
        seatch_y_pos += 1
    if isVisible:
        return True

    isVisible = True
    search_y_pos = len(forest[search_x_pos]) - 1
    while isVisible and search_y_pos > position_y:
        isVisible = forest[position_x][search_y_pos] < current_tree
        search_y_pos -= 1
    if isVisible:
        return True

    return False


input_file = open("input.txt", "r")
matrix = []

for line in input_file:
    if line[-1]=='\n':
        matrix.append(list(line)[:-1])
    else:
        matrix.append(list(line))

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix[i][j]= int(matrix[i][j])

print(matrix)

total_sum = 0

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        total_sum = total_sum + 1 if tree_is_visible(matrix, i, j) else total_sum

print("Trees can be seen: ",total_sum)