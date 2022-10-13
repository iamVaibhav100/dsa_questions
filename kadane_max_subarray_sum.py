def max_subarray_sum(arr):
    max_sum = max(arr)
    curr_sum = 0

    for i in arr:
        if curr_sum < 0:
            curr_sum = 0
        curr_sum += i
        max_sum = max(curr_sum, max_sum)

    return max_sum

print(max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]))