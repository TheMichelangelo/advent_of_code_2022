def replace(string, position, symbol):
    tmp = list(string)
    tmp[position] = symbol
    string = ''.join(tmp)
    return string


def move_boxes(boxes, move_from, move_to):
    position_line = boxes[-1]
    position_box_from = position_line.find(str(move_from))
    position_box_to = position_line.find(str(move_to))
    line_num_iterator = 0
    while boxes[line_num_iterator][position_box_from] == ' ' and line_num_iterator < (len(boxes) - 1):
        line_num_iterator += 1
    letter = ''
    if line_num_iterator < (len(boxes) - 1):
        letter = boxes[line_num_iterator][position_box_from]
        boxes[line_num_iterator] = replace(boxes[line_num_iterator], position_box_from - 1, ' ')
        boxes[line_num_iterator] = replace(boxes[line_num_iterator], position_box_from + 1, ' ')
        boxes[line_num_iterator] = replace(boxes[line_num_iterator], position_box_from, ' ')

    line_num_iterator = 0
    while boxes[line_num_iterator][position_box_to] == ' ' and line_num_iterator < (len(boxes) - 1):
        line_num_iterator += 1

    line_num_iterator -= 1
    if line_num_iterator == -1:
        boxes.insert(0, ' ' * len(boxes[-1]))
        line_num_iterator = 0

    if letter != '':
        boxes[line_num_iterator] = replace(boxes[line_num_iterator], position_box_to - 1, '[')
        boxes[line_num_iterator] = replace(boxes[line_num_iterator], position_box_to + 1, ']')
        boxes[line_num_iterator] = replace(boxes[line_num_iterator], position_box_to, letter)


input_file = open("input.txt", "r")
total_sum_points = 0

line = ""
lines_with_boxes = []

while line != '\n':
    line = input_file.readline()
    lines_with_boxes.append(line[:-1])
lines_with_boxes.remove('')
max_line_len = len(lines_with_boxes[-1]) + 1
empty_line = ' ' * max_line_len

for i in range(0, len(lines_with_boxes)):
    if len(lines_with_boxes[i]) < max_line_len:
        lines_with_boxes[i] = lines_with_boxes[i] + ' ' * (max_line_len - len(lines_with_boxes[i]))
    print(lines_with_boxes[i])

for line in input_file:
    print(line)
    splited_line = line.split(" ")
    amount_to_move = int(splited_line[1])
    move_from = int(splited_line[3])
    move_to = int(splited_line[5])
    for i in range(0, amount_to_move):
        move_boxes(lines_with_boxes, move_from, move_to)
        if lines_with_boxes[0] == empty_line:
            lines_with_boxes.remove(empty_line)
    for line in lines_with_boxes:
        print(line)

for line in lines_with_boxes:
    print(line)
