# def minCost1(colors, neededTime) -> int:
#     min_time = 0
#     for i in range(len(colors) - 1):
#         if colors[i] == colors[i + 1]:
#             min_time += min(neededTime[i], neededTime[i + 1])
#
#     return min_time

def minCost2(s, cost) -> int:
    left, ans = 0, 0
    for right in range(1, len(s)):
        if s[left] == s[right]:
            if cost[left] < cost[right]:
                ans += cost[left]
            else:
                ans += cost[right]
                # If right is cheaper, delete right and kept left
                # position for next step calculation
                continue

        left = right
    return ans

# print(minCost1("abaac",[1,2,3,4,5]))
print(minCost2("abaac",[1,2,3,4,5]))