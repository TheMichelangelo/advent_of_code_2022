def check_any_overlap(group_one, group_two):
    group_one_sections = group_one.split("-")
    group_two_sections = group_two.split("-")
    group_one_start = int(group_one_sections[0])
    group_one_end = int(group_one_sections[1])
    group_two_start = int(group_two_sections[0])
    group_two_end = int(group_two_sections[1])

    if group_two_end < group_one_start or group_one_end < group_two_start:
        return False
    return True


input_file = open("input.txt", "r")
total_sum_points = 0

for line in input_file:
    groups = line.split(",")
    if check_any_overlap(groups[0], groups[1].replace('\n', '')):
        total_sum_points = total_sum_points + 1

print("Total overlapping sections: ", total_sum_points)
