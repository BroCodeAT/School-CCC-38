from dataclasses import dataclass


def load_file(filename: str = "level2/level2_1.in") -> list:
    with open(filename, "r") as file:
        return [line.strip() for line in file.readlines()][1:]


def write_to_file(pieces, counts, filename: str = "level2/level2_1.out") -> None:
    with open(filename, "w") as file:
        for piece, count in zip(pieces, counts):
            file.write(str(count) + " " + str(piece) + "\n")


@dataclass
class Piece:
    top: str
    right: str
    bottom: str
    left: str

    rotated = 0

    def __str__(self):
        return f"{self.top},{self.right},{self.bottom},{self.left}"

    def __eq__(self, other: "Piece"):
        if self.top == other.top and self.right == other.right and self.bottom == other.bottom and self.left == other.left:
            return True
        return False

    def __init__(self, data: str):
        self.top, self.right, self.bottom, self.left = data.split(",")

    def rotate(self):
        self.top, self.right, self.bottom, self.left = self.left, self.top, self.right, self.bottom
        self.rotated += 1
        if self.rotated == 4:
            self.rotated = 0

    def match(self, other: "Piece", side: str):
        if side == "top":
            return self.top == other.bottom
        elif side == "right":
            return self.right == other.left
        elif side == "bottom":
            return self.bottom == other.top
        elif side == "left":
            return self.left == other.right


def main(data: list):
    data = [[Piece(piece) for piece in line.split(" ")] for line in data]
    pieces = []
    counts = []
    for piece in data:
        in_flag = False
        for i in range(4):
            if piece in pieces:
                in_flag = True
                counts[pieces.index(piece)] += 1
                break
            else:
                piece.rotate()
        if not in_flag:
            pieces.append(piece)
            counts.append(1)
    # Count if a piece is equal to another piece in any rotation and count them
    return counts, pieces


if __name__ == '__main__':
    count, pieces = main(load_file(f"level3/level3_example.in"))
    write_to_file(pieces, count, f"level3/level3_example.out")

    for i in range(1, 6):
        count, pieces = main(load_file(f"level3/level3_{i}.in"))
        write_to_file(pieces, count, f"level3/level3_{i}.out")
