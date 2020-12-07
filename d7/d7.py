from typing import List
import gzip
import networkx as nx


def read(file: str) -> List[str]:
    with gzip.open(file, "rt") as f:
        return [i for i in f.read().split("\n") if len(i) > 0]


def count(curr, G):
    return sum(v["weight"] * count(nxt, G) for nxt, v in G.get(curr, {}).items()) + 1


def main():
    arr = read("input_d7.txt.gz")
    G = nx.DiGraph()
    for row in arr:
        split = row.split()
        key = " ".join(row.split()[:2])
        values = list(
            map(
                lambda x: (x.split()[0], " ".join(x.split()[1:-1])),
                row[row.find("contain") + 8 :].split(","),
            )
        )
        if ("no", "other") in values:
            continue
        G.add_weighted_edges_from([(v[1], key, int(v[0])) for v in values])

    print("Task 1:", len(list(nx.dfs_edges(G, "shiny gold"))))
    print("Task 2:", count("shiny gold", nx.to_dict_of_dicts(nx.reverse(G))) - 1)


if __name__ == "__main__":
    main()
