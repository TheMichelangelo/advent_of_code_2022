def build_section_row(section_start, section_end):
    string_with_sections = ""
    for i in range(section_start, section_end + 1, 1):
        string_with_sections += str(i)
    return string_with_sections


def check_overlap_wrong_legacy(group_one, group_two):
    group_one_sections = group_one.split("-")
    group_two_sections = group_two.split("-")
    group_one_sections_str = build_section_row(int(group_one_sections[0]), int(group_one_sections[1]))
    group_two_sections_str = build_section_row(int(group_two_sections[0]), int(group_two_sections[1]))
    print(group_one_sections_str.find(group_two_sections_str))
    print(group_two_sections_str.find(group_one_sections_str))
    if group_one_sections_str.find(group_two_sections_str) != -1 or group_two_sections_str.find(
            group_one_sections_str) != -1:
        print(int(group_one_sections[0]), "-",int(group_one_sections[1]),",",int(group_two_sections[0]), "-",int(group_two_sections[1]))
        return True
    return False


def check_overlap(group_one, group_two):
    group_one_sections = group_one.split("-")
    group_two_sections = group_two.split("-")
    group_one_start = int(group_one_sections[0])
    group_one_end = int(group_one_sections[1])
    group_two_start = int(group_two_sections[0])
    group_two_end = int(group_two_sections[1])

    if group_one_start <= group_two_start and group_one_end >= group_two_end:
        return True
    if group_two_start <= group_one_start and group_two_end >= group_one_end:
        return True
    return False


input_file = open("input.txt", "r")
total_sum_points = 0

for line in input_file:
    groups = line.split(",")
    if check_overlap(groups[0], groups[1].replace('\n', '')):
        total_sum_points = total_sum_points + 1

print("Total overlapping sections: ", total_sum_points)
