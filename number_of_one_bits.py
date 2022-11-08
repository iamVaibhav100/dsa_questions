# Write a function that takes an unsigned integer and returns the number of '1' bits it has
# (also known as the Hamming weight).

# Explanation:
# The key idea is to realize that for any number n, doing a bit-wise AND of n and n - 1 flips the
# least-significant 1-bit in n to 0. Why? Consider the binary representations of n and n - 1. In
# the binary representation of n, the least significant 1-bit in n must be in a 0-bit followed by
# some 1-bits. Therefore, n - 1 must have the same 1-bits as n, except that its least significant
# 1-bit must be flipped. Therefore, doing a bit-wise AND of n and n - 1 flips the least significant
# 1-bit in n to 0, and keeps all other bits the same.

def hamming_weight(n: int) -> int:
    count = 0
    while n:
        count += 1
        n &= n - 1
    return count

print(hamming_weight(11111111111111111111111111111101))
