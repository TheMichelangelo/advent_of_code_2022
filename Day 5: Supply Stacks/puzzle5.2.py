def replace(string, position, symbol):
    tmp = list(string)
    tmp[position] = symbol
    string = ''.join(tmp)
    return string


def move_boxes(boxes, move_from, move_to, amount):
    position_line = boxes[-1]
    position_box_from = position_line.find(str(move_from))
    position_box_to = position_line.find(str(move_to))
    line_num_iterator = 0
    while boxes[line_num_iterator][position_box_from] == ' ' and line_num_iterator < (len(boxes) - 1):
        line_num_iterator += 1
    letter = ''
    if line_num_iterator >= (len(boxes) - 1):
        return
    letters = []
    for j in range(0, amount):
        letter = boxes[line_num_iterator + j][position_box_from]
        letters.append(letter)
        boxes[line_num_iterator + j] = replace(boxes[line_num_iterator + j], position_box_from - 1, ' ')
        boxes[line_num_iterator + j] = replace(boxes[line_num_iterator + j], position_box_from + 1, ' ')
        boxes[line_num_iterator + j] = replace(boxes[line_num_iterator + j], position_box_from, ' ')

    for j in range(0, amount):
        boxes.insert(0, ' ' * len(boxes[-1]))

    line_num_iterator = 0
    while boxes[line_num_iterator][position_box_to] == ' ' and line_num_iterator < (len(boxes) - 1):
        line_num_iterator += 1
    line_num_iterator -= 1

    if len(letters) == 0:
        return

    for i in range(0, len(letters), 1):
        boxes[line_num_iterator - i] = replace(boxes[line_num_iterator - i], position_box_to - 1, '[')
        boxes[line_num_iterator - i] = replace(boxes[line_num_iterator - i], position_box_to + 1, ']')
        boxes[line_num_iterator - i] = replace(boxes[line_num_iterator - i], position_box_to,
                                               letters[len(letters) - 1 - i])


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
    move_boxes(lines_with_boxes, move_from, move_to, amount_to_move)
    while lines_with_boxes[0] == empty_line:
        lines_with_boxes.remove(empty_line)
    for line in lines_with_boxes:
        print(line)

for line in lines_with_boxes:
    print(line)
