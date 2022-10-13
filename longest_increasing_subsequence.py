# DP problem
# brute-force - O(N^2) Space - O(N)
# def lengthOfLIS(nums) -> int:
#     n = len(nums)
#     dp = [1] * n
#     for i in range(n):
#         for j in range(i):
#             if nums[i] > nums[j] and dp[i] < dp[j] + 1:
#                 dp[i] = dp[j] + 1
#     return max(dp)
#
# print(lengthOfLIS([2,1,6,3,5,4,10]))

# Greedy with Binary Search - O(NlogN)
from bisect import bisect_left
def lengthOfLIS(nums) -> int:
    sub = []
    for x in nums:
        if len(sub) == 0 or sub[-1] < x:
            sub.append(x)
        else:
            idx = bisect_left(sub, x)  # Find the index of the first element >= x
            sub[idx] = x  # Replace that number with x
    return len(sub)

print(lengthOfLIS([2,1,6,3,5,4,10]))