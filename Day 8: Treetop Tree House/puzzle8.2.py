def countScenicScore(forest: list, position_x: int, position_y: int) -> int:
    upScore = 0
    search_x_pos = position_x - 1

    current_tree = forest[position_x][position_y]
    while search_x_pos >= 0 and forest[search_x_pos][position_y] < current_tree:
        search_x_pos -= 1
        upScore += 1

    if search_x_pos > 0:
        upScore += 1

    downScore = 0
    search_x_pos = position_x + 1
    while search_x_pos < len(forest[position_x]) and forest[search_x_pos][position_y] < current_tree:
        search_x_pos += 1
        downScore += 1

    if search_x_pos < len(forest[position_x]):
        downScore += 1

    leftScore = 0
    search_y_pos = position_y - 1
    while search_y_pos >= 0 and forest[position_x][search_y_pos] < current_tree:
        search_y_pos -= 1
        leftScore += 1

    if search_y_pos > 0 :
        leftScore += 1

    rightScore = 0
    search_y_pos = position_y + 1
    while search_y_pos < len(forest[position_x]) and forest[position_x][search_y_pos] < current_tree:
        search_y_pos += 1
        rightScore += 1

    if search_y_pos < len(forest[position_x]) :
        rightScore += 1

    return upScore * downScore * leftScore * rightScore


input_file = open("input.txt", "r")
matrix = []

for line in input_file:
    if line[-1] == '\n':
        matrix.append(list(line)[:-1])
    else:
        matrix.append(list(line))

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix[i][j] = int(matrix[i][j])

print(matrix)

max_count_scenic_score = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        scenic_score = countScenicScore(matrix, i, j)
        max_count_scenic_score = scenic_score if scenic_score > max_count_scenic_score else max_count_scenic_score

print("Trees can be seen: ", max_count_scenic_score)
