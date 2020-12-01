from typing import List
import itertools
import math
import gzip

def read(file) -> List[int]:
    with gzip.open(file) as f:
        return [int(i.strip()) for i in f.readlines()]


def find(arr: List[int], n: int, target: int) -> List[int]:
    return [q for q in itertools.combinations(arr, n) if sum(q) == target]


def main():
    arr = read("input.csv.gz")
    target = 2020
    res2 = find(arr, 2, target)[0]
    print(res2, math.prod(res2))
    res3 = find(arr, 3, target)[0]
    print(res3, math.prod(res3))


if __name__ == "__main__":
    main()
