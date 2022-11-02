def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    hash_map = {}
    ans = []
    for i in nums1:
        hash_map[i] = hash_map.get(i, 0) + 1

    for j in nums2:
        if j in hash_map and hash_map[j] > 0:
            hash_map[j] -= 1
            ans.append(j)

    return ans

print(intersect([4,9,5], [9,4,9,8,4]))