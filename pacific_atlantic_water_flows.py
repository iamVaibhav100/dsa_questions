def pacificAtlantic(heights: list[list[int]]) -> list[list[int]]:
    rows, cols = len(heights), len(heights[0])
    p_visited = set()
    a_visited = set()
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def dfs(i, j, visited):
        if (i, j) in visited:
            return
        visited.add((i, j))

        for dr, dc in directions:
            nxt_i, nxt_j = dr + i, dc + j
            if 0 <= nxt_i < rows and 0 <= nxt_j < cols:
                if heights[nxt_i][nxt_j] >= heights[i][j]:
                    dfs(nxt_i, nxt_j, visited)

    for row in range(rows):
        dfs(row, 0, p_visited)
        dfs(row, cols - 1, a_visited)

    for col in range(cols):
        dfs(0, col, p_visited)
        dfs(rows - 1, col, a_visited)

    return list(p_visited & a_visited)