from day1.day1 import get_input_lines, solve_part_one, solve_part_two

input_path = "tests/test_input1.txt"
lines = get_input_lines(input_path)


def test_solve_part_one():
    hit_zero_count = solve_part_one(lines)
    assert hit_zero_count == 3


def test_solve_part_two():
    lines = get_input_lines(input_path)
    cross_zero_count = solve_part_two(lines)
    assert cross_zero_count == 6
