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

    rotated = 0

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

    def rotate(self):
        self.top, self.right, self.bottom, self.left = self.left, self.top, self.right, self.bottom
        self.rotated += 1
        if self.rotated == 4:
            self.rotated = 0


def main(data: list) -> list:
    pieces = [Piece(piece) for piece in data]
    for piece in pieces:

    return data


if __name__ == '__main__':
    comp = main(load_file(f"level2/level2_example.in"))
    write_to_file(comp, f"level2/level2_example.out")

    for i in range(1, 6):
        comp = main(load_file(f"level2/level2_{i}.in"))
        write_to_file(comp, f"level2/level2_{i}.out")
