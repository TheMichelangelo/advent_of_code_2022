def find_first_set_unique(text, needed_amount):
    letters = []
    max_index = needed_amount
    for i in range(0, needed_amount):
        letters.append(text[i])

    while len(letters) != needed_amount or len(letters) != len(set(letters)):
        letters.pop(0)
        letters.append(text[max_index])
        max_index += 1
    return max_index


input_file = open("input.txt", "r")
line_with_message = input_file.readline()
print('First set starting 4 starts: ', find_first_set_unique(line_with_message,4))
print('First set starting 4 starts: ', find_first_set_unique(line_with_message,14))
