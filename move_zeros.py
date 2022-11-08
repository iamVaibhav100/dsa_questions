def moveZeroes(nums: list[int]) -> None:
    n = len(nums)
    p = n - 1
    for i in range(n):
        while nums[p] == 0:
            p -= 1
        if nums[i] == 0:
            nums[i], nums[p] == nums[p], nums[i]
            p -= 1

    return nums

print(moveZeroes([0,1,0,3,12]))