def maximumMultiple(N, A) -> int:
    A.sort()
    c = 0

    for i in A:
        if i < 0:
            c += 1

    if 2 * c == N:
        A = A[(N//2)-1::-1] + A[N//2:]

    maxi = -1e18
    for i in range(N):
        maxi = max(maxi, A[i] * A[N-i-1])

    return maxi

print(maximumMultiple(8, [-11, 8, 10, 9, -19,-8, 19, -14]))