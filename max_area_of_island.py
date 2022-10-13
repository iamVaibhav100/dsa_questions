from collections import deque

# BFS solution
# def max_area_of_island(grid: list[list[int]]) -> int:
#     r, c = len(grid), len(grid[0])
#     max_area: int = 0
#     directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
#
#     def bfs(i, j):
#         q = deque([(i, j)])
#         grid[i][j] = 0
#         area = 0
#
#         while q:
#             nr, nc = q.popleft()
#             area += 1
#
#             for dr, dc in directions:
#                 nxt_r = nr + dr
#                 nxt_c = nc + dc
#
#                 if 0 <= nxt_r < r and 0 <= nxt_c < c and grid[nxt_r][nxt_c] == 1:
#                     grid[nxt_r][nxt_c] = 0
#                     q.append((nxt_r, nxt_c))
#         return area
#
#     for i in range(r):
#         for j in range(c):
#             if grid[i][j] == 1:
#                 max_area = max(max_area, bfs(i, j))
#
#     return max_area

# DFS Solution
def max_area_of_island(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])
    DIR = [0, 1, 0, -1, 0]

    def dfs(r, c):
        if r < 0 or r == m or c < 0 or c == n or grid[r][c] == 0:
            return 0
        ans = 1
        grid[r][c] = 0  # Mark this square as visited
        for i in range(4):
            ans += dfs(r + DIR[i], c + DIR[i + 1])
        return ans

    ans = 0
    for r in range(m):
        for c in range(n):
            ans = max(ans, dfs(r, c))
    return ans

print(max_area_of_island([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))