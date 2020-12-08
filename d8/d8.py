from typing import List, Tuple
import gzip


def read(file: str) -> List[Tuple[str, int]]:
    with gzip.open(file, "rt") as f:
        return [(l.split()[0], int(l.split()[1])) for l in f.read().strip().split("\n")]


def run(prog: List[Tuple[str, int]]) -> Tuple[int, bool]:
    acc = 0
    curr = 0
    visited = []
    while curr < len(prog):
        if curr >= len(prog) or curr in visited:
            return acc, False
        visited.append(curr)
        op, i = prog[curr]
        curr += [1, i][op == "jmp"]
        acc += [0, i][op == "acc"]
    return acc, True


def main():
    prog = read("input_d8.txt.gz")
    acc, ok = run(prog)
    print(f"task 1: {acc=}")
    for i, row in enumerate(prog):
        if row[0] not in ("jmp", "nop"):
            continue
        p = prog.copy()
        p[i] = ["jmp", "nop"][row[0] == "jmp"], row[1]
        acc, ok = run(p)
        if ok:
            print(f"task 2: {acc=}")


if __name__ == "__main__":
    main()
