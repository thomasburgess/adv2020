import gzip
import re

KEYS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
EYES = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def read(file: str):
    with gzip.open(file, "rt") as f:
        return map(
            lambda x: dict(i.split(":") for i in x if ":" in i),
            (re.split(r"\n|\s", i) for i in f.read().split("\n\n")),
        )


def check1(line):
    line["cid"] = None
    return len(set(line).intersection(KEYS)) == len(KEYS)


def check2(line):
    if not check1(line):
        return False

    try:
        byr = int(line["byr"])
        if (byr < 1920) or (byr > 2002):
            return False
        iyr = int(line["iyr"])
        if (iyr < 2010) or (iyr > 2020):
            return False
        eyr = int(line["eyr"])
        if (eyr < 2020) or (eyr > 2030):
            return False
    except:
        return False

    hgt = line["hgt"]
    if "in" in hgt:
        hgt = int(hgt[:-2])
        if (hgt < 59) or (hgt > 76):
            return False
    elif "cm" in hgt:
        hgt = int(hgt[:-2])
        if (hgt < 150) or (hgt > 193):
            return False
    else:
        return False

    if (
        (re.search(r"#([A-F|a-f|0-9]{6})$", line["hcl"]) == None)
        or (line["ecl"] not in EYES)
        or (sum(c.isdigit() for c in line["pid"]) != 9)
    ):
        return False

    return True


def main():
    arr = read("input_d4.txt.gz")
    print(sum(map(check1, arr)))
    arr = read("input_d4.txt.gz")
    print(sum(map(check2, arr)))


if __name__ == "__main__":
    main()
