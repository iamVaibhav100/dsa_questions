def outer_trees(trees):
    def calculate_equation(p1, p2, p3):
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3
        return (y3 - y1) * (x2 - x1) - (y2 - y1) * (x3 - x1)

    trees.sort()
    upper = []
    lower = []
    for p in trees:
        while len(upper) >= 2 and calculate_equation(upper[-2], upper[-1], p) > 0:
            upper.pop()
        while len(lower) >= 2 and calculate_equation(lower[-2], lower[-1], p) < 0:
            lower.pop()
        upper.append(tuple(p))
        lower.append(tuple(p))

    return list(set(upper + lower))

print(outer_trees([[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]))