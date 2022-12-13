from copy import deepcopy
from typing import List, Tuple, Iterable
from functools import cmp_to_key


filename = "./solutions/13/data.txt"

ListItem = Iterable[int]


def find_closing_bracket(s: str, start: int) -> int:
    starting_brackets = 0
    for i, c in enumerate(s[start:]):
        if c == "[":
            starting_brackets += 1
        elif c == "]":
            starting_brackets -= 1
            if starting_brackets == 0:
                return i
    return -1


def parse_line(line: str) -> ListItem:
    item = []
    s = line[1:][:-1]
    skip = -1
    next_num = ""
    for i, c in enumerate(s):
        if i <= skip:
            continue
        if c == "," or c == "]":
            if next_num:
                item.append(int(next_num))
                next_num = ""
        elif c == "[":
            end = find_closing_bracket(s, i)
            skip = end + 1
            item.append(parse_line(s[i:][: end + 1]))
        else:
            next_num += c
    if next_num:
        item.append(int(next_num))
    return item


def get_data(filename: str) -> List[Tuple[ListItem, ListItem]]:
    items: List[Tuple[ListItem, ListItem]] = []
    with open(filename, "r") as f:
        lines = [line.strip() for line in f.readlines()]
        next_pair: List[ListItem] = [0, 0]
        for i, line in enumerate(lines):
            j = (i + 1) % 3
            if j == 0:
                items.append(tuple(next_pair))
            else:
                next_pair[j - 1] = parse_line(line)
        items.append(next_pair)
    return items


def compare(l1: ListItem, l2: ListItem) -> bool:
    for i in range(len(l1)):
        if i >= len(l2):
            return False
        x, y = l1[i], l2[i]
        c = None
        if type(x) == int == type(y):
            if x < y:
                return True
            elif x > y:
                return False
        elif type(x) == int:
            c = compare([x], y)
        elif type(y) == int:
            c = compare(x, [y])
        else:
            c = compare(x, y)
        if c == None:
            continue
        return c
    if len(l1) < len(l2):
        return True
    return None


def sorter(l1: ListItem, l2: ListItem) -> int:
    if str(l1) == str(l2):
        return 0
    return -1 if compare(l1, l2) else 1


def part1(items: List[Tuple[ListItem, ListItem]]) -> int:
    return sum([i + 1 for i, pair in enumerate(items) if compare(*pair)])


def part2(items: List[Tuple[ListItem, ListItem]]) -> int:
    d1, d2 = [[2]], [[6]]
    items_copy = deepcopy(items)
    items_copy.append((d1, d2))
    items_flat = [item for pair in items_copy for item in pair]
    items_flat.sort(key=cmp_to_key(sorter))
    i, j = items_flat.index(d1), items_flat.index(d2)
    return (i + 1) * (j + 1)


items = get_data(filename)

print(part1(items))
print(part2(items))
