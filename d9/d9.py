from typing import List
import gzip
from itertools import combinations


def read(file: str) -> List[int]:
    with gzip.open(file, "rt") as f:
        return list(map(int, f.read().strip().split("\n")))


def find_break(arr: List[int], length: int) -> int:
    for i, n in enumerate(arr[length:]):
        preamble = arr[i : i + length]
        ok = False
        for a, b in combinations(preamble, 2):
            if a + b == n:
                ok = True
                break
        if not ok:
            return n


def find_preamble(arr: List[int], n: int) -> int:
    for i, start in enumerate(arr):
        if start > n:
            continue
        s = start
        for j, end in enumerate(arr[i + 1 :], i + 1):
            s += end
            if s == n:
                return min(arr[i : j + 1]) + max(arr[i : j + 1])
            if s > n:
                break


def main():
    arr = read("input_d9.txt.gz")
    length = 25
    n = find_break(arr, length)
    print(f"Part 1 {n=}")
    w = find_preamble(arr, n)
    print(f"Part 2 {w=}")


if __name__ == "__main__":
    main()
