import collections


def four_sum_2(a, b, c, d):
    ab = collections.Counter(u + v for u in a for v in b)
    return sum(ab[-(u + v)] for u in c for v in d)

print(four_sum_2([1, 2], [-2, -1], [-1, 2], [0, 2]))