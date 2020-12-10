from typing import List
import gzip
import collections


def read(file: str) -> List[int]:
    with gzip.open(file, "rt") as f:
        return list(sorted(map(int, f.read().strip().split("\n"))))


def main():
    arr = read("input_d10.txt.gz")
    count = collections.Counter([1] + [j - i for i, j in zip(arr[:-1], arr[1:])] + [3])
    print(f"Task 1 {count[1]*count[3]}")
    agg = {0: 1}
    for l in arr:
        agg[l] = sum(agg.get(l - i, 0) for i in range(1, 4))
    print("task 2", agg[max(agg)])


if __name__ == "__main__":
    main()
