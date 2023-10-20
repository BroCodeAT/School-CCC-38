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
    top: bool
    right: bool
    bottom: bool
    left: bool

    rotated = 0

    def __str__(self):
        return f"{'K' if self.top else 'H'},{'K' if self.right else 'H'},{'K' if self.bottom else 'H'},{'K' if self.left else 'H'}"

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


def main(data: list):
    data = [Piece(piece) for piece in data]
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
    count, pieces = main(load_file(f"level2/level2_example.in"))
    write_to_file(pieces, count, f"level2/level2_example.out")

    for i in range(1, 6):
        count, pieces = main(load_file(f"level2/level2_{i}.in"))
        write_to_file(pieces, count, f"level2/level2_{i}.out")
