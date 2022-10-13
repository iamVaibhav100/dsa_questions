def superFunctionalStrings(s):
    length = len(s) + 1
    modu=10**9 + 7
    substrs = {s[j:i] for j in range(length) for i in range(j+1, length)}
    return sum(len(b) ** len(set(b)) for b in substrs) % modu

print(superFunctionalStrings("abc"))