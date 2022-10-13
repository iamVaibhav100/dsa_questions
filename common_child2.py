s1 = input().upper()
s2 = input().upper()

l1 = list(s1)
l2 = list(s2)
w = sorted(l1)
z = sorted(l2)

def check():
    if w == z:
        return len(s1) - 1
    sum = []
    largest = 0
    for i in range(len(s1)):
        if s1[i] in s2:
            index = s2.index(s1[i])
            for j in range(index,len(s2)):
                if s1[i] == s2[j]:
                    largest +=1
            sum.append(largest)
    if len(sum) == 0:
        return 0
    else:
        return max(sum) - 1

print(check())