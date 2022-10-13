def minRemoveToMakeValid(self, s: str) -> str:
    stack = []
    new = s
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)

        elif s[i] == ')':
            if len(stack) == 0:
                new = s.replace(s[i], "", 1)
            else:
                stack.pop()

    if len(stack) == 0:
        return new
    elif len(stack) == 1 and len(new) == len(s):
        return s.replace('(', '', 1)
    else:
        return ""

print(minRemoveToMakeValid("a)b(c)d"))