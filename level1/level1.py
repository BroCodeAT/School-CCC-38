from dataclasses import dataclass

def load_file(filename: str = "level1/level1_1.in") -> list:
    with open(filename, "r") as file:
        return [line.strip() for line in file.readlines()][1:]


def write_to_file(data: list, filename: str = "level1/level1_1.out") -> None:
    with open(filename, "w") as file:
        for line in data:
            file.write(line + "\n")


def main(data: list) -> list:
    return data


if __name__ == '__main__':
    for i in range(1, 2):
        comp = main(load_file(f"level1/level1_{i}.in"))
        write_to_file(comp, f"level1/level1_{i}.out")
