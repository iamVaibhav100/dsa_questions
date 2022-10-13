import math
from collections import Counter

cases = int(input())
for i in range(cases):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))

    uni_len = len(set(a))

    if len(set(a)) == 1:
        print(1)

    elif k >= n:
        print(1)

    elif (uni_len != n):
        l = []
        dict = Counter(a)
        print(dict)
        for key, value in dict.items():
            if value == 1:
                l.append(key)

    else:
        print(math.ceil(n/k))