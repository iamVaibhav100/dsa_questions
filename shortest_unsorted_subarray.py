# sort solution: O(nlogn)
def findUnsortedSubarray1(nums):
    is_same = [a == b for a, b in zip(nums, sorted(nums))]
    return 0 if all(is_same) else len(nums) - is_same.index(False) - is_same[::-1].index(False)

# Without sort: O(n)
def findUnsortedSubarray2(nums):
    if len(nums) < 2: return 0

    l, r = 0, len(nums) - 1

    while l < len(nums) - 1 and nums[l] <= nums[l + 1]:
        l += 1

    while r > 0 and nums[r] >= nums[r - 1]:
        r -= 1

    if l > r:
        return 0

    temp = nums[l:r + 1]
    tempMin = min(temp)
    tempMax = max(temp)

    while l > 0 and tempMin < nums[l - 1]:
        l -= 1

    while r < len(nums) - 1 and tempMax > nums[r + 1]:
        r += 1

    return r - l + 1

print(findUnsortedSubarray1([2,3,4,8,7,6,5,1,11,10]))