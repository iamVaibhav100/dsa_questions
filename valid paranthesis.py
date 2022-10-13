def isValid(s: str) -> bool:
    if len(s) == 0:
        return True
    paran = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    stack = []

    for i in range(len(s)):
        if s[i] in paran:
            stack.append(s[i])
        else:
            if len(stack) != 0:
                right = stack.pop()
                if paran[right] != s[i]:
                    return False
            else:
                return False
    return len(stack) == 0

print(isValid("(("))
