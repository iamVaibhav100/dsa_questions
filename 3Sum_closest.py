def threeSumClosest(nums, target) -> int:
    nums.sort()
    result = nums[0] + nums[1] + nums[2]
    for i in range(len(nums) - 2):

        if i > 0 and nums[i] == nums[i - 1]:
            continue

        l, r = i + 1, len(nums) - 1
        while l < r:
            curSum = nums[l] + nums[r] + nums[i]
            if curSum == target:
                return target
            if abs(curSum - target) < abs(result - target):
                result = curSum
            if curSum < target:
                l += 1
            else:
                r -= 1
    return result

# Recursive solution for K sum closest not only 3 pairs.

# def threeSumClosest(nums, target) -> int:
#     nums.sort()
#     return kSumClosest(nums, 3, target)
#
# def kSumClosest(self, nums, k, target):
#     N = len(nums)
#     # Special case where we only have k elements in nums. Return only option
#     if N == k:
#         return sum(nums[:k])
#
#     # special case where the target is way too low
#     # we give the lowest we can
#     if sum(nums[:k]) >= target:
#         return sum(nums[:k])
#
#     # special case where the target is too high
#     # we give the largest we can
#     if sum(nums[-k:]) <= target:
#         return sum(nums[-k:])
#
#     # base case. look for the closest element
#     if k == 1:
#         # the element is the first and the delta is the second
#         deltas = [(x, abs(target - x)) for x in nums]
#         return min(deltas, key=lambda x: x[1])[0]
#
#     # pick one element out and recursively search for closest match with k being one less
#     closest = sum(nums[:k])
#     for i, x in enumerate(nums):
#         # small optimization to handle duplicate x values
#         if i > 0 and nums[i - 1] == x:
#             continue
#
#         bestMatch = self.kSumClosest(nums[i + 1:], k - 1, target - x)
#         current = x + bestMatch
#         if abs(target - current) < abs(target - closest):
#             if target == current:
#                 return current
#             else:
#                 closest = current
#
#     return closest

print(threeSumClosest([4,0,5,-5,3,3,0,-4,-5],-2))