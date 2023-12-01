"""Advent of Code. Day 1."""
import re

file = open("day1/input.txt")

line_nums = []
for line in file:
    line_digits = [i for i in line.rstrip() if i.isdigit()]
    line_nums.append(int(line_digits[0] + line_digits[-1]))

print(f"Day 1, Task 1 Solution: {sum(line_nums)}")


numbers = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


def replace_number_words(line: str) -> str:
    """Insert digits where number words are found."""
    found = []
    for idx, number in enumerate(numbers):
        occur_idx = [m.start() for m in re.finditer(number, line)]
        for num_idx in occur_idx:
            found.append((num_idx, idx))
    found = sorted(found)
    for idx, thing in enumerate(found):
        loc, num = thing
        line = line[: loc + idx] + str(num) + line[loc + idx :]
    return line


file.seek(0)
line_nums_2 = []

for line in file:
    clean_line = replace_number_words(line.rstrip())
    line_digits = [i for i in clean_line if i.isdigit()]

    comb = int(line_digits[0] + line_digits[-1])
    line_nums_2.append(comb)

print(f"Day 1, Task 2 Solution: {sum(line_nums_2)}")
