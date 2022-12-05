variant_to_points = {"A": 1, "B": 2, "C": 3}


def get_points_for_variant(player_variant, elf_variant):
    if player_variant == "Y":
        return variant_to_points[elf_variant]
    if player_variant == "X" and elf_variant != "A":
        return variant_to_points[elf_variant] - 1
    elif player_variant == "X" and elf_variant == "A":
        return 3
    if player_variant == "Z" and elf_variant != "C":
        return variant_to_points[elf_variant] + 1
    elif player_variant == "Z" and elf_variant == "C":
        return 1


def calculate_result_points(player_variant, elf_variant):
    if player_variant == "X":  # player placed rock
        return 0 + get_points_for_variant(player_variant, elf_variant)
    elif player_variant == "Y":  # player placed paper
        return 3 + get_points_for_variant(player_variant, elf_variant)
    else:  # scissors
        return 6 + get_points_for_variant(player_variant, elf_variant)


input_file = open("input.txt", "r")
total_sum_points = 0

for line in input_file:
    variants = line.split()
    total_sum_points += calculate_result_points(variants[1][0], variants[0])

print("Total points get: ", total_sum_points)
