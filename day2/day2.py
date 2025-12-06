def get_file_content(input_path: str):
    with open(input_path) as f:
        return f.read().split(",")


def solve_part_one(filecontent: list[str]):
    bad_ids: list[int] = []
    for id_range in filecontent:
        start, finish = map(int, id_range.split("-", 2))
        for id in range(start, finish + 1):
            id = str(id)
            if id[: len(id) // 2] == id[len(id) // 2 : len(id)]:
                bad_ids.append(int(id))
    return sum(bad_ids)


## TODO: not correct, fix it
def solve_part_two(filecontent: list[str]):
    bad_ids: list[int] = []
    for id_range in filecontent:
        start, finish = map(int, id_range.split("-", 2))
        for id in range(start, finish + 1):
            id = str(id)
            if id[: len(id) // 2] == id[len(id) // 2 : len(id)]:
                bad_ids.append(int(id))
    return sum(bad_ids)


def main():
    path = "input.txt"
    lines = get_file_content(path)
    sum_bad_ids = solve_part_one(lines)
    sum_two = solve_part_two(lines)
    print(f"Day 2 part 1: {sum_bad_ids}")
    print(f"Day 2 part 2: {sum_two}")


if __name__ == "__main__":
    main()
