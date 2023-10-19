def load_file(filename: str = "level3/level3_1.in") -> list:
    with open(filename, "r") as file:
        return [line.strip() for line in file.readlines()]


def write_to_file(data: list, filename: str = "level3/level3_1.out") -> None:
    with open(filename, "w") as file:
        for line in data:
            file.write(line + "\n")


def main(data: list) -> list:
    return data


if __name__ == '__main__':
    for i in range(1, 6):
        comp = main(load_file(f"level3/level3_{i}.in"))
        write_to_file(comp, f"level3/level3_{i}.out")
