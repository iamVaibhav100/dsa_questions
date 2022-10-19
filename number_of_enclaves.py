def numEnclaves(grid: list[list[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    def dfs(i, j):
        grid[i][j] = 0

        for dr, dc in directions:
            nr, nc = i + dr, j + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                dfs(nr, nc)

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1 and (i == 0 or i == rows - 1 or j == 0 or j == cols - 1):
                dfs(i, j)

    return sum(sum(row) for row in grid)

print(numEnclaves())