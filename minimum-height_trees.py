from collections import defaultdict


# Brute force approach - O(N^2)
# def findMinHeightTrees(n, E):
#     G, seen = defaultdict(set), [False] * n
#     for u, v in E:
#         G[u].add(v)
#         G[v].add(u)
#
#     def dfs(i):
#         if seen[i]: return 0
#         seen[i] = True
#         H = 1 + max((dfs(adj) for adj in G[i]), default=0)
#         seen[i] = False
#         return H
#
#     for i in range(n):
#         H = dfs(i)
#         if H < min_H:
#             min_H = H
#             ans.clear()
#         if H == min_H:
#             ans.append(i)
#     return ans

# 2nd approach Remove Leaves using BFS - O(N)
# There can be max 2 roots possible if number of nodes are odd then 1 if even then 2 roots
# removing leaf nodes until 2 or 1 nodes are left that will be answer.
def findMinHeightTrees(n, edges):
    if n <= 2:
        return [node for node in range(n)]

    graph = defaultdict(set)
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)

    leaves = []
    for i in range(n):
        if len(graph[i]) == 1:
            leaves.append(i)

    remaining_nodes = n
    while remaining_nodes > 2:
        remaining_nodes -= len(leaves)
        new_leaves = []

        for leaf in leaves:
            for node in graph[leaf]:
                graph[node].remove(leaf)
                if len(graph[node]) == 1:
                    new_leaves.append(node)
        leaves = new_leaves

    return leaves

# 3nd approach using only 2 DFS to find the longest path calls - O(N)
# def findMinHeightTrees(n, E):
#     G, seen = defaultdict(set), [False] * n
#     for u, v in E:
#         G[u].add(v)
#         G[v].add(u)
#
#     def dfs(i):
#         if seen[i]: return []
#         longest_path = []
#         seen[i] = True
#         for adj in G[i]:
#             if not seen[adj]:
#                 path = dfs(adj)
#                 if len(path) > len(longest_path):
#                     longest_path = path
#         longest_path += [i]
#         seen[i] = False
#         return longest_path
#
#     path = dfs(dfs(0)[0])
#     return {path[len(path) // 2], path[(len(path) - 1) // 2]}

print(findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]]))