from itertools import cycle, islice
# def saveThePrisoner(n, m, s):
#     arr = [i for i in range(1, n + 1)]
#     p = list(islice(cycle(arr), s-1, m+1))
#
#     print(p)
#     print(arr)
#     return p[len(p) - 1]
#
#
def saveThePrisoner(n, m, s):
    return ((m+s-2)%n+1)


print(saveThePrisoner(3,7,3))
