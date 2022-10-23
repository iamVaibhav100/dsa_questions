# solution 1 - using maths
def findErrorNums1(nums):
    n = len(nums)
    A = -sum(nums) + n * (n + 1) // 2
    B = -sum(i * i for i in nums) + n * (n + 1) * (2 * n + 1) // 6
    return [(B - A * A) // 2 // A, (B + A * A) // 2 // A]

# solution 2
def findErrorNums2(self, nums):
    return [sum(nums) - sum(set(nums)), sum(range(1, len(nums)+1)) - sum(set(nums))]


print(findErrorNums1([2, 3, 2]))