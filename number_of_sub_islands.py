def countSubIslands(grid1: list[list[int]], grid2: list[list[int]]) -> int:
    rows, cols = len(grid1), len(grid1[0])
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    count = 0

    def dfs(i, j):
        if i not in (0, rows) or j not in (0, cols):
            return

        for dr, dc in directions:
            nr, nc = dr + i, dc + j

            if 0 <= nr < rows and 0 <= nc < cols and grid1[nr][nc] == 1 and grid2[nr][nc] == 1:
                grid2[nr][nc] = 0

                dfs(nr, nc)

    for i in range(rows):
        for j in range(cols):
            if grid1[i][j] == 1 and grid2[i][j] == 1:
                count += 1
                grid2[i][j] = 0
                dfs(i, j)

    return count

print(countSubIslands([[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]))