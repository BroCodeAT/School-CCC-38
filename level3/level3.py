from dataclasses import dataclass


def load_file(filename: str = "level2/level2_1.in") -> list:
    with open(filename, "r") as file:
        return [line.strip() for line in file.readlines()][1:]


def write_to_file(data, filename: str = "level2/level2_1.out") -> None:
    with open(filename, "w") as file:
        file.write("\n".join([" ".join([str(piece) for piece in line]) for line in data]))


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
        for i in range(4):
            if self.top == other.top and self.right == other.right and self.bottom == other.bottom and self.left == other.left:
                return True
            self.rotate()
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

            return self.top != other.bottom and self.top != "E" and other.bottom != "E"
        elif side == "right":
            return self.right != other.left and self.right != "E" and other.left != "E"
        elif side == "bottom":
            return self.bottom != other.top and self.bottom != "E" and other.top != "E"
        elif side == "left":
            return self.left != other.right and self.left != "E" and other.right != "E"


def main(data: list):
    data = [[Piece(piece) for piece in line.split(" ")] for line in data]
    for ind_line, line in enumerate(data):
        for ind_piece, piece in enumerate(line):
            if not piece.right == "E":
                while not piece.match(data[ind_line][ind_piece+1], "right"):
                    piece.right = "K" if piece.right == "H" else "H"
            if not piece.bottom == "E":
                while piece.match(data[ind_line+1][ind_piece], "bottom"):
                    piece.bottom = "K" if piece.bottom == "H" else "H"

    return data


if __name__ == '__main__':
    data = main(load_file(f"level3/level3_example.in"))
    print("\n".join([" ".join([str(piece) for piece in line]) for line in data]))
    write_to_file(data, f"level3/level3_example.out")

    for i in range(1, 6):
        data = main(load_file(f"level3/level3_{i}.in"))
        write_to_file(data, f"level3/level3_{i}.out")
