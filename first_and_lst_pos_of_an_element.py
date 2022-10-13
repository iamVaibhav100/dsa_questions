class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if len(nums) == 0:
            return [-1, -1]

        def binarySearch(nums, left, right, target):
            while left <= right:
                mid = (left + right) // 2
                if target == nums[mid]:
                    return mid
                elif target > nums[mid]:
                    left += mid
                else:
                    right -= mid
            return -1

        firstPos = binarySearch(nums, 0, len(nums) - 1, target)
        if firstPos == -1:
            return [-1, -1]

        startPos = firstPos
        endPos = firstPos
        temp1, temp2 = 0, 0

        while startPos != -1:
            temp1 = startPos
            startPos = binarySearch(nums, 0, startPos - 1, target)
        startPos = temp1

        while endPos != -1:
            temp2 = endPos
            endPos = binarySearch(nums, endPos + 1, len(nums) - 1, target)
        endPos = temp2

        return [startPos, endPos]

sol = Solution()
print(sol.searchRange([1,1,2], 1))