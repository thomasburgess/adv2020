from typing import List
import gzip

def read(file: str) -> List[List[str]]:
    with gzip.open(file, "rt") as f:
        return [[j for j in i.split("\n") if len(j)>0] for i in f.read().split("\n\n")]

def nyes1(group: List[str]) -> int:
    return len(set("".join(group)))

def nyes2(group: List[str]) -> int:
    return len(set.intersection(*[set(s) for s in group]))

def main():
    arr = read("input_d6.txt.gz")
    print(sum(map(nyes1, arr)))
    print(sum(map(nyes2, arr)))

if __name__ == '__main__':
    main()