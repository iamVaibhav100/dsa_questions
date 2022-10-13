def minJumps(nums, n):
    on_place = 0
    jumps = 0
    distance = 0
    for i in range(len(nums)-1):
        distance = max(distance,i+nums[i])
        if i==on_place:
            on_place = distance
            jumps += 1
        if i >= distance:
            return -1
    return jumps

print(minJumps([1,3,5,7,2,8,9,10], 8))