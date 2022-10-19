# You are given a string of lowercase letters, you need to find a letter which comes in the string consecutively (
# continuous occurrence) for most of time. If their are more than one letter which occur most of the time then you
# should return the letter which occurs first in the string. You have to find the letter as well as the count of its
# occurrence

def count(n: int, s: str) -> list[str]:
    count = 1
    max_count = 0
    max_char = s[0]
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            count += 1
        else:
            if count > max_count:
                max_count = count
                max_char = s[i]
            count = 1
    return [max_char, max_count]

print(count(6, "aabbbb"))