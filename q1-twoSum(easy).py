# Given an array of int, return the indices of two numbers that add up to a given target.
# e.g. array = [1, 2, 3, 5, 7] and target = 4
# return [0, 2]

a = map(int, input("Enter elements of the array: ").split())
target = int(input("Enter the target: "))
arr = list(a)

def two_sum(arr, target):
    num_map = {}
    for i in range(len(arr)):
        try:
            num = num_map[arr[i]]
            return [num, i]
        except:
            num = target - arr[i]
            num_map[num] = i
    return None

print(two_sum(arr, target))

