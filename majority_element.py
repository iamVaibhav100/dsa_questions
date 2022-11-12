# Time Complexity: O(nlogn)
# Space Complexity: O(1)
def majority_element_1(nums):
    # Sort the list
    nums.sort()
    # Return the middle element
    return nums[len(nums)//2]

# Using Hashmap
# Time Complexity: O(n)
# Space Complexity: O(n)
def majority_element_2(nums):
    # Create a hashmap
    hashmap = {}
    # Iterate through the list
    for i in nums:
        # If the element is in the hashmap
        if i in hashmap:
            # Increment the value
            hashmap[i] += 1
        # Otherwise
        else:
            # Add the element to the hashmap
            hashmap[i] = 1
    # Return the key with the max value
    return max(hashmap, key=hash)



# Using Boyer-Moore Voting Algorithm
# Time Complexity: O(n)
# Space Complexity: O(1)
def majority_element_3(nums):
    # Set the count to 0
    count = 0
    # Iterate through the list
    for i in nums:
        # If the count is 0
        if count == 0:
            # Set the candidate to the current element
            candidate = i
        # If the current element is the candidate
        if i == candidate:
            # Increment the count
            count += 1
        # Otherwise
        else:
            # Decrement the count
            count -= 1
    # Return the candidate
    return candidate

print(majority_element_3([3, 2, 3, 2, 4, 5, 5, 5, 8]))