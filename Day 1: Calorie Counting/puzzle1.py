input_file = open("input.txt", "r")
elf_calories = []
current_sum = 0
for line in input_file:
    if line == '\n':
        elf_calories.append(current_sum)
        current_sum = 0
    else:
        current_sum += int(line[:-1])

elf_calories_sorted_by_amount = sorted(elf_calories, reverse=True)

print("Max sum carried: ", elf_calories_sorted_by_amount[0])

print("Total sum of 3 elfs with most calories carried: ",
      elf_calories_sorted_by_amount[0] + elf_calories_sorted_by_amount[1] + elf_calories_sorted_by_amount[2])
