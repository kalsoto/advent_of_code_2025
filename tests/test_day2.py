from day2.day2 import get_file_content, solve_part_one, solve_part_two

input_path = "tests/test_input2.txt"
file_content = get_file_content(input_path)


def test_solve_part_one():
    sum_bad_ids = solve_part_one(file_content)
    assert sum_bad_ids == 1227775554


def test_solve_part_two():
    sum_bad_ids = solve_part_two(file_content)
    assert sum_bad_ids == 4174379265
