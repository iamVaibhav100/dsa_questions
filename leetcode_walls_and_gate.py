import collections


def wall_and_gate(matrix: list[list[int]]):
    rows, cols = len(matrix), len(matrix[0])
    visited = set()

    def bfs(matrix, r, c, visited):
        q = collections.deque()
        q.append((r,c))
        visited.add((r,c))

        while q:
            row, col = q.popleft()
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            for dr, dc in directions:
                r, c = row+dr, col+dc
                if r in range(rows) and c in range(cols) and (r,c) not in visited and matrix[r][c] == -10:
                    q.append((r,c))
                    visited.add((r,c))
                    matrix[r][c] = matrix[r][c] + 1

    for r in range(rows):
        for c in range(cols):
            if (r,c) not in visited and matrix[r][c] == 0:
                bfs(matrix,r,c,visited)
    return matrix

print(wall_and_gate([[-10,-1,0,-10], [-10,-10,-10,-1], [-10,-1,-10,-1], [0,-1,-10,-10]]))