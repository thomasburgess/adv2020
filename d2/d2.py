from typing import List, Tuple
import re
import gzip


def read(file) -> List[int]:
    with gzip.open(file, "rt") as f:
        return f.readlines()


def match(line: str) -> Tuple[int, int, chr, str]:
    m = re.match(r"(\d*)-(\d*).(\S):.(\S*)", line)
    return (int(m.group(1)), int(m.group(2)), m.group(3), m.group(4))


def check1(entry: Tuple[int, int, chr, str]) -> bool:
    n = entry[3].count(entry[2])
    return (n >= entry[0]) and (n <= entry[1])


def check2(entry: Tuple[int, int, chr, str]) -> bool:
    return (entry[3][entry[0] - 1] == entry[2]) ^ (entry[3][entry[1] - 1] == entry[2])


def main():
    arr = read("input_d2.txt.gz")
    print("part1", sum(check1(i) for i in map(match, arr)))
    print("part1", sum(check2(i) for i in map(match, arr)))


if __name__ == "__main__":
    main()
