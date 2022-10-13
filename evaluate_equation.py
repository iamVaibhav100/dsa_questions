from collections import defaultdict

#
def calcEquation(equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
    graph = defaultdict(dict)
    for (x, y), val in zip(equations, values):
        graph[x][y] = val
        graph[y][x] = 1.0 / val

    def dfs(x, y, visited):
        if x not in graph or y not in graph:
            return -1

        if y in graph[x]:
            return graph[x][y]

        for node in graph[x]:
            if node not in visited:
                visited.add(node)
                val = dfs(node, y, visited)
                if val == -1:
                    continue
                else:
                    return graph[x][node] * val

        return -1

    res = []
    for q in queries:
        res.append(dfs(q[0], q[1], set()))

    return res

print(calcEquation([["a","b"],["b","c"],["bc","cd"]], [1.5,2.5,5.0], [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]))