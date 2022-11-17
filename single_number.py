# What is XOR?
# XOR is a binary operation that takes two equal-length binary strings and produces
# another string of the same length as the inputs.
# The result of XOR is 1 if and only if the inputs differ at that position.

# The XOR operation is also known as the modulus 2 addition or subtraction.
# Example:
# 1 ^ 1 = 0
# 1 ^ 0 = 1
# 0 ^ 1 = 1
# 0 ^ 0 = 0
# 230 ^ 102 = 128 (10001110 ^ 01100110 = 11100000)


def single_number(nums):
    res = 0
    for i in nums:
        res ^= i
    return res


print(single_number([2, 2, 1]))

