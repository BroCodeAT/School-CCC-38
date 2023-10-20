from dataclasses import dataclass


def load_file(filename: str = "level2/level2_1.in") -> list:
    with open(filename, "r") as file:
        return [line.strip() for line in file.readlines()]


def write_to_file(data: list, filename: str = "level2/level2_1.out") -> None:
    with open(filename, "w") as file:
        for line in data:
            file.write(line + "\n")


@dataclass
class Piece:
    top: bool
    right: bool
    bottom: bool
    left: bool

    def __eq__(self, other: "Piece"):
        if self.top == other.top and self.right == other.right and self.bottom == other.bottom and self.left == other.left:
            return True
        return False

    def __init__(self, data: str):
        data = data.split(",")
        self.top = True if data[0] == "K" else False
        self.right = True if data[1] == "K" else False
        self.bottom = True if data[2] == "K" else False
        self.left = True if data[3] == "K" else False


def main(data: list) -> list:
    pieces = [Piece(piece) for piece in data]
    return data


if __name__ == '__main__':
    for i in range(1, 6):
        comp = main(load_file(f"level2/level2_{i}.in"))
        write_to_file(comp, f"level2/level2_{i}.out")
