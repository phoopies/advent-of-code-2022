from FileSystem import FileSystem
from Folder import Folder
from File import File

filename = "./solutions/7/data.txt"


def get_data(filename: str) -> FileSystem:
    fs = FileSystem()
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            s = line.strip()
            if s.startswith("$"):
                c = s[2:].split(" ")
                command, args = c[0], c[1:]
                fs.handle_command(command, args)
            else:
                if s.startswith("dir"):
                    dir_name = s.split(" ")[-1]
                    fs.add(Folder(dir_name, None))
                else:
                    size, fname = s.split(" ")
                    fs.add(File(fname, int(size)))
    return fs


def part1(fs: FileSystem, threshold=100000) -> int:
    f_sizes_flat = fs.root.get_folder_sizes_flat()
    return sum([s for s in f_sizes_flat if s <= threshold])


def part2(
    fs: FileSystem,
    total_disk_space: int = 70000000,
    required_disk_space: int = 30000000,
) -> int:
    if total_disk_space < required_disk_space:
        return -1

    used_disk_space = fs.root.size()
    disk_space_left = total_disk_space - used_disk_space
    disk_space_needed = required_disk_space - disk_space_left
    if disk_space_needed <= 0:
        return 0

    f_sizes_flat = fs.root.get_folder_sizes_flat()
    f_sizes_flat_big_enough = [
        size for size in f_sizes_flat if size >= disk_space_needed
    ]
    return min(f_sizes_flat_big_enough)


fs = get_data(filename)

print(part1(fs))
print(part2(fs))
