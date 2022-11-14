from collections import defaultdict


# using dfs
def remove_stones_1(stones: list[list[int]]) -> int:
    graph_x = defaultdict(list)
    graph_y = defaultdict(list)
    for x, y in stones:
        graph_x[x].append(y)
        graph_y[y].append(x)

    def dfs(xo, yo):
        nonlocal visited
        if (xo, yo) not in visited:
            visited.add((xo, yo))
            for neiY in graph_x[xo]:
                dfs(xo, neiY)
            for neiX in graph_y[yo]:
                dfs(neiX, yo)

    connected_component = 0
    visited = set()
    for x, y in stones:
        if (x, y) not in visited:
            dfs(x, y)
            connected_component += 1

    return len(stones) - connected_component


# using union find
def remove_stones_2(stones: list[list[int]]) -> int:
    UF = {}

    def find(x):
        if x != UF[x]:
            UF[x] = find(UF[x])
        return UF[x]

    def union(x, y):
        if x not in UF:
            UF[x] = x
        if y not in UF:
            UF[y] = y
        rootX = find(x)
        rootY = find(y)
        UF[rootX] = rootY

    maxX = 10 ** 4
    for x, y in stones:
        union(x, y + maxX)

    return len(stones) - len({find(n) for n in UF})


print(remove_stones_2([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]))
