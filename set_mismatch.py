def findErrorNums(nums):
    n = len(nums)
    A = -sum(nums) + n * (n + 1) // 2
    B = -sum(i * i for i in nums) + n * (n + 1) * (2 * n + 1) // 6
    return [(B - A * A) // 2 // A, (B + A * A) // 2 // A]

print(findErrorNums([2, 3, 2]))