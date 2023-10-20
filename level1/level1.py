def load_file(filename: str = "level1/level1_1.in") -> list:
    with open(filename, "r") as file:
        return [line.strip() for line in file.readlines()][1:]


def write_to_file(pieces, counts, filename: str = "level1/level1_1.out") -> None:
    with open(filename, "w") as file:
        for piece, count in zip(pieces, counts):
            file.write(str(count) + " " + piece + "\n")


def main(data: list):
    pieces:list[str] = []
    counts:list[int] = []
    for line in data:
        if line not in pieces:
            pieces.append(line)
    for piece in pieces:
        counts.append(data.count(piece))
    return pieces, counts


if __name__ == '__main__':
    for i in range(1, 2):
        pieces, counts = main(load_file(f"level1/level1_example.in"))
        write_to_file(pieces, counts, f"level1/level1_example.out")