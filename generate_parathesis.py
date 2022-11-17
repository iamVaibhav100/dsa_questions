def generate_parenthesis(n: int) -> list[str]:

    def dfs(left, right, s):
        if len(s) == 2 * n:
            res.append(s)
            return res

        if left < n:
            dfs(left + 1, right, s + '(')
        if right < left:
            dfs(left, right + 1, s + ')')

    res = []
    dfs(0, 0, '')
    return res


print(generate_parenthesis(3))

