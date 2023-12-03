"""Advent of Code. Day 3."""
import os
import re


def find_symbol_for_id(number: int, index: tuple, lines: list[str]) -> list:
    """Look around numbers for any symbols and return them."""
    x, y1, y2 = index
    found = []
    # generate indexes to search, above, middle, below
    search_space = [(x - 1, y1 - 1, y2 + 1), (x, y1 - 1, y2 + 1), (x + 1, y1 - 1, y2 + 1)]
    for i, i1, i2 in search_space:
        if i >= 0 and i < len(lines):
            i1 = 0 if i1 < 0 else i1
            i2 = len(lines[i]) if i2 > len(lines[i]) else i2
            matched_syms = re.search(r"[^\w .\s]", lines[i][i1:i2])
            if matched_syms is not None:
                z1, z2 = matched_syms.span()
                found.append((number, matched_syms.group(), i, z1 + i1))
    if len(found) > 0:
        return found


def parse_lines(lines: list[str]) -> list:
    """Parse the lines into a schematic."""
    clean_lines = [x.rstrip() for x in lines]
    numbers_map = []
    for line_idx, line in enumerate(clean_lines):
        numbers = re.finditer(r"(\d+)", line)
        for number in numbers:
            numbers_map.append((number.group(), (line_idx, *number.span())))
    valid_ids = []
    for found_num, indexes in numbers_map:
        found_sym = find_symbol_for_id(found_num, indexes, clean_lines)
        if found_sym is not None:
            valid_ids.extend(found_sym)
    return valid_ids


def part_1(lines: list[str]) -> int:
    """Solve Part 1."""
    valid_ids = parse_lines(lines)
    total = 0
    for valid_id, _, _, _ in valid_ids:
        total += int(valid_id)
    return total


def part_2(lines: list[str]) -> int:
    """Solve Part 2."""
    valid_ids = parse_lines(lines)
    gear_map = {}
    for valid_id, symbol, symbol_row, symbol_pos in valid_ids:
        if symbol == "*":
            gear_key = f"{symbol_row}_{symbol_pos}"
            if gear_key in gear_map:
                gear_map[gear_key].append(valid_id)
            else:
                gear_map[gear_key] = [valid_id]
    total = 0
    for _, value in gear_map.items():
        if len(value) == 2:
            total += int(value[0]) * int(value[1])

    return total


if __name__ == "__main__":
    lines = []
    dir_path = os.path.dirname(os.path.realpath(__file__))

    # Load in the input
    # with open(f"{dir_path}/test_input.txt") as f:
    with open(f"{dir_path}/input.txt") as f:
        lines = f.readlines()

    # Solve Part 1
    part_1_answer = part_1(lines)
    print(f"Day 3. Part 1: {part_1_answer}")

    # solve Part 2
    part_2_answer = part_2(lines)
    print(f"Day 3. Part 2: {part_2_answer}")
