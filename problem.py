def subtractProductAndSum(n: int) -> int:
    numbers = list(str(n))
    s = 0
    p = 1
    for i in numbers:
        s += int(i)
        p = p * int(i)
    return p - s

print(subtractProductAndSum(234))