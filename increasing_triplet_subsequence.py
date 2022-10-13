from bisect import bisect_left
def increasingTriplet(nums) -> bool:
    sub = []

    for i in nums:
        if len(sub) == 0 or sub[-1] < i:
            sub.append(i)
            if len(sub) == 3:
                return True
        else:
            idx = bisect_left(sub, i)
            sub[idx] = i

    return False

print(increasingTriplet([1, 5, 0, 1, 4, 1, 3]))