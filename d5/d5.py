from typing import List
import gzip


def read(file: str) -> List[str]:
    with gzip.open(file, "rt") as f:
        return f.read().split("\n\n")


def divide(code: str, upper: int) -> int:
    lo = 0
    up = upper
    for s in code[:7]:
        mid = (up - lo + 1) // 2
        if s in ("F", "L"):
            up -= mid
        else:
            lo += mid
    return lo


def proc(code: str):
    row = divide(code[:7], upper=127)
    seat = divide(code[7:], upper=8)
    seat_id = row * 8 + seat
    return seat_id


def main():
    arr = read("input_d5.txt.gz")
    print(f"Max seat_id {max(map(proc, arr))}")
    q = sorted(map(proc, arr))
    print(f"Gap {[(a, b) for a,b in zip(q[1:], q[:-1]) if abs(a-b)>1]}")


if __name__ == "__main__":
    main()
