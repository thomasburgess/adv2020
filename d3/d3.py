from typing import List
import gzip


def read(file: str) -> List[str]:
    with gzip.open(file, "rt") as f:
        return [i for i in f.read().split("\n") if len(i) > 0]


def traverse(arr: List[str], right: int, down: int) -> int:
    x = 0
    y = 0
    trees = 0
    while y < len(arr) - 1:
        x = (x + right) % len(arr[y])
        y += down
        if arr[y][x] == "#":
            trees += 1
    return trees


def main():
    arr = read("input_d3.txt.gz")
    mul = 1
    for right, down in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)):
        t = traverse(arr, right, down)
        mul *= t
        print(right, down, t)
    print(mul)


if __name__ == "__main__":
    main()
