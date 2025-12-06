def get_input_lines(input_path: str):
    with open(input_path) as f:
        return f.readlines()


def solve_part_one(lines: list[str]):
    dial_position, hit_zero_count = 50, 0
    for line in lines:
        direction = 1 if line[0] == "R" else -1
        dial_position += direction * int(line[1:])
        dial_position %= 100

        if dial_position == 0:
            hit_zero_count += 1
    return hit_zero_count


def solve_part_two(lines: list[str]):
    dial_position, cross_zero_count = 50, 0
    for line in lines:
        direction = 1 if line[0] == "R" else -1
        for i in range(int(line[1:])):
            dial_position += direction
            dial_position %= 100
            if dial_position == 0:
                cross_zero_count += 1
    return cross_zero_count


def main():
    path = "input.txt"
    lines = get_input_lines(path)

    hit_zero_count = solve_part_one(lines)
    print(hit_zero_count)

    cross_zero_count = solve_part_two(lines)
    print(cross_zero_count)


if __name__ == "__main__":
    main()
