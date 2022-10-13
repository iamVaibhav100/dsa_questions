#You are given an integer array height of length n. There are n vertical lines drawn such that
# the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container,
# such that the container contains the most water.
# Return the maximum amount of water a container can store.

def maxArea(height):
    if len(height) <= 1:
        return 0
    if len(height) == 2:
        return min(height[0], height[1])

    p1 = 0
    p2 = len(height) - 1
    max_area = 0
    while (p1 < p2):
        h = min(height[p1], height[p2])
        w = p2 - p1
        area = h * w
        max_area = max(max_area, area)
        if (height[p1] <= height[p2]):
            p1 += 1
        else:
            p2 -= 1
    return max_area