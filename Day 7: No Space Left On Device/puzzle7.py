def buildFileSystem(system_space: dict, folder_path: any, content: list):
    if folder_path not in system_space.keys() or system_space[folder_path] == 0:
        for element in content:
            parts = element.split()
            if element[0] == 'd':
                if len(folder_path) == 1:
                    new_path = folder_path + parts[1]
                else:
                    new_path = folder_path + '/' + parts[1]
                system_space[new_path] = 0
            else:
                new_size = system_space[folder_path] + int(parts[0])
                system_space[folder_path] = new_size


def createFileSystemIerarhy(iterable_input_file) -> dict:
    system_space = {'/': 0}
    base_path = ''
    for line in iterable_input_file:
        line = line[:-1]

        if line.startswith('$ ls'):
            items = []
            while not line.startswith('$ cd'):
                line = next(iterable_input_file, None)
                if line is not None:
                    items.append(line)
                else:
                    break
            if line is not None:
                items.remove(line)
            buildFileSystem(system_space, base_path, items)
            if line is None:
                break
        if line.startswith('$ cd') and line.split()[2] == '..':
            base_path = base_path[:base_path.rfind('/')]
            if len(base_path) == 0:
                base_path = '/'
        else:
            if len(base_path) == 1:
                base_path += line.split()[2]
            elif len(base_path) != 0:
                base_path = base_path + '/' + line.split()[2]
            else:
                base_path = line.split()[2]

    return system_space


def calculate_each_folder_size(system_space: dict) -> dict:
    list_of_dirs = system_space.keys()
    total_folder_sizes = {}

    for dir in list_of_dirs:
        subdir = list(filter(lambda x: x.startswith(dir), list_of_dirs))
        total_size = 0
        for tmp in subdir:
            total_size += system_space[tmp]
        total_folder_sizes[dir] = total_size
    return total_folder_sizes


input_file = open("input.txt", "r")

total_sum = 0
iterable_input_file = iter(input_file)
system_space = createFileSystemIerarhy(iterable_input_file)

# print('\n'.join(system_space))
for key in system_space.keys():
    total_sum += system_space[key]

# print('CALCULATED SIZE')

system_space_by_folders = calculate_each_folder_size(system_space)
# print('\n'.join(system_space_by_folders))

sum_folders_less_then_10000 = 0
for key in system_space_by_folders.keys():
    if (system_space_by_folders[key] < 100000):
        sum_folders_less_then_10000 += system_space_by_folders[key]

print("Total size", total_sum)
print("Total size less then 100000", sum_folders_less_then_10000)

folders_sorted_by_size = dict(sorted(system_space_by_folders.items(), key=lambda item: item[1], reverse=True))
print(folders_sorted_by_size)

print("Space left:", 70000000 - system_space_by_folders['/'],
      '. Need at least:', 30000000 - (70000000 - system_space_by_folders['/']))

neededSpace = 30000000 - (70000000 - system_space_by_folders['/'])
folder_names = list(folders_sorted_by_size.keys())
name_index = 0

while system_space_by_folders[folder_names[name_index]] > neededSpace:
    name_index += 1

print("Folder with space:", folder_names[name_index - 1], ". Size ",
      system_space_by_folders[folder_names[name_index - 1]])
print("Folder with space:", folder_names[name_index], ". Size ", system_space_by_folders[folder_names[name_index]])
print(neededSpace + system_space_by_folders[folder_names[name_index - 1]], ' : ',
      system_space_by_folders[folder_names[name_index]])
