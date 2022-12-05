map_player_to_elf_placement = {"X": "A", "Y": "B", "Z": "C"}


def get_win_points(player_variant, elf_variant):
    if player_variant == elf_variant:
        return 3
    if player_variant == "C" and elf_variant == "A":
        return 0
    if player_variant > elf_variant or (player_variant == "A" and elf_variant == "C"):
        return 6
    return 0


def calculate_result_points(player_variant, elf_variant):
    if player_variant == "A":  # player placed rock
        return 1 + get_win_points(player_variant, elf_variant)
    elif player_variant == "B":  # player placed paper
        return 2 + get_win_points(player_variant, elf_variant)
    else:  # scissors
        return 3 + get_win_points(player_variant, elf_variant)


input_file = open("input.txt", "r")
total_sum_points = 0

for line in input_file:
    variants = line.split()
    total_sum_points += calculate_result_points(map_player_to_elf_placement[variants[1][0]], variants[0])

print("Total points get: ", total_sum_points)
