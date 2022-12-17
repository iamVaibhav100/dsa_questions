
def eval_rpn(tokens: list[str]) -> int:
    operations = {
        "*": lambda x, y: x * y,
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "/": lambda x, y: float(x) / y
    }

    stack = []
    for token in tokens:
        if token not in operations:
            stack.append(int(token))
        else:
            right = stack.pop()
            left = stack.pop()
            result = operations[token](left, right)
            stack.append(int(result))
    return stack.pop()


if __name__ == "__main__":
    print(eval_rpn(["2", "1", "+", "3", "*"]))
    print(eval_rpn(["4", "13", "5", "/", "+"]))
    print(eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))

