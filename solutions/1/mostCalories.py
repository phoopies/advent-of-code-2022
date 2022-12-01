from os.path import exists
from typing import List, Tuple
from functools import reduce

filename = "./solutions/1/data.txt"

def get_data(filename: str) -> List[str]:
  data = [0]
  with open(filename, 'r') as f:
    lines = f.readlines()
    for line in lines:
      stripped = line.strip()
      if stripped:
        data[-1] += int(stripped)
      else:
        data.append(0)
  return data

def part1(data):
  return max(data)

def part2(data: List[int], count: int = 3):
  if len(data) <= count:
    return sum(data)
  
  most_calories_carrying_elves: List[int] = []
  total_calories: List[int] = []
  for _ in range(count):
    worst_elves = [calories for elf, calories in enumerate(data) if elf not in most_calories_carrying_elves]
    most_calories = part1(worst_elves)
    best_elf_of_the_worst = data.index(most_calories)

    total_calories.append(most_calories)
    most_calories_carrying_elves.append(best_elf_of_the_worst)
  
  return sum(total_calories)

data = get_data(filename)
print(part1(data))
print(part2(data))