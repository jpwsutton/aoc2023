"""Advent of Code. Day 2."""
import re


def parse_line(line: str) -> dict:
    """Parse a line into a dict."""
    parsed_line = {}
    # Get the Game ID and the rounds
    split = re.findall(r"(\d+)\:(.*)", line)[0]
    rounds = split[1].split(";")
    p_rounds = []
    for round in rounds:
        tokens = re.findall(r"((\d+)\s*(red|blue|green))", round)
        d = {"red": 0, "blue": 0, "green": 0}
        for _, col_count, colour in tokens:
            d[colour] = int(col_count)
        p_rounds.append(d)
    parsed_line["game"] = split[0]
    parsed_line["rounds"] = p_rounds
    parsed_line["max_t"] = {k: max(d[k] for d in p_rounds) for k in p_rounds[0].keys()}
    parsed_line["min_power"] = (
        parsed_line["max_t"]["red"] * parsed_line["max_t"]["green"] * parsed_line["max_t"]["blue"]
    )

    return parsed_line


def part_1(lines: list[str]) -> int:
    """Solve Part 1."""
    parsed_lines = [parse_line(x.rstrip()) for x in lines]

    filter = {"red": 12, "green": 13, "blue": 14}
    valid_games = [
        game for game in parsed_lines if (all(game["max_t"].get(key) <= value for key, value in filter.items()) is True)
    ]
    valid_id_sum = sum([int(game["game"]) for game in valid_games])

    return valid_id_sum


def part_2(lines: list[str]) -> int:
    """Solve Part 2."""
    parsed_lines = [parse_line(x.rstrip()) for x in lines]
    total_powers = sum(game["min_power"] for game in parsed_lines)
    return total_powers


if __name__ == "__main__":
    lines = []
    # Load in the input
    with open("day2/input.txt") as f:
        # with open("day2/test_input.txt") as f:

        lines = f.readlines()

    # Solve Part 1
    part_1_answer = part_1(lines)
    print(f"Day 2. Part 1: {part_1_answer}")

    # solve Part 2
    part_2_answer = part_2(lines)
    print(f"Day 2. Part 2: {part_2_answer}")
