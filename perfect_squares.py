# Question: 279. Perfect Squares
# Link: https://leetcode.com/problems/perfect-squares/
# Description: Given a positive integer n, find the least number of perfect square numbers.
# (for example, 1, 4, 9, 16, ...) which sum to n.

# Example 1: Input: n = 12, Output: 3 Explanation: 12 = 4 + 4 + 4.
# Example 2: Input: n = 13, Output: 2 Explanation: 13 = 4 + 9.


# using dp
def num_square(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = i
        j = 1
        while j * j <= i:
            dp[i] = min(dp[i], dp[i - j * j] + 1)
            j += 1

    return dp[n]

print(num_square(12))

# using bfs
def num_square2(n):
    if n <= 0:
        return 0
    queue = [n]
    level = 0
    while queue:
        level += 1
        next_queue = []
        for i in queue:
            j = 1
            while j * j <= i:
                if i - j * j == 0:
                    return level
                next_queue.append(i - j * j)
                j += 1
        queue = next_queue

    return level

print(num_square2(12))

# using math (fastest)
# Time complexity: O(n)
def num_square3(n):
    if n <= 0:
        return 0
    while n % 4 == 0:
        n /= 4
    if n % 8 == 7:
        return 4
    a = 0
    while a * a <= n:
        b = int((n - a * a) ** 0.5)
        if a * a + b * b == n:
            if a != 0 and b != 0:
                return 2
            else:
                return 1
        a += 1

    return 3

print(num_square3(12))
