def matrixRotation(matrix, r):
    for i in range(m):
        for j in range(1, n):
            matrix[i][j-1] = matrix[i][j]
    print(matrix)


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    r = int(first_multiple_input[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
