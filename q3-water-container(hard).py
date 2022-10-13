# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it can trap after raining.


# brute force method
# def trap(height):
#     if len(height) <= 1:
#         return 0
#     total_water = 0
#     for i in range(len(height)):
#         maxL = 0
#         maxR = 0
#         for j in range(i + 1, len(height)):
#             if height[j] > maxR:
#                 maxR = height[j]
#         for k in range(i - 1, -1, -1):
#             if height[k] > maxL:
#                 maxL = height[k]
#
#         water = min(maxL, maxR) - height[i]
#         if water > 0:
#             total_water += water
#
#     return total_water
#
# print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))

# Optimized solution
def trap(height):
    if len(height) <= 1:
        return 0
    total_water = 0
    left = 0
    right = len(height) - 1
    maxL = 0
    maxR = 0
    while left < right:
        if height[left] <= height[right]:
            if height[left] >= maxL:
                maxL = height[left]
            else:
                total_water = total_water + (maxL - height[left])
            left += 1
        else:
            if height[right] >= maxR:
                maxR = height[right]
            else:
                total_water = total_water + (maxR - height[right])
            right -= 1

    return total_water

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))

