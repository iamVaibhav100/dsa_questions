def make_string_great(s: str) -> str:
    stack = []

    for c in s:
        if stack and stack[-1] == c.swapcase():
            stack.pop()
        else:
            stack.append(c)

    return "".join(stack)

print(make_string_great("abBAcC"))