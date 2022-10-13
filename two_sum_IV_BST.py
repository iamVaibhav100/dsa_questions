# This solution does uses the fact that given tree is a bst

# def findTarget(root, k: int) -> bool:
#     def dfs(root, seen):
#         if root == None: return False
#         complement = k - root.val
#         if complement in seen: return True
#         seen.add(root.val)
#         return dfs(root.left, seen) or dfs(root.right, seen)
#
#     return dfs(root, set())

# Solution 2 - Using BST property
# def findTarget(root, k: int) -> bool:
#     def pushLeft(st, root):
#         while root:
#             st.append(root)
#             root = root.left
#
#     def pushRight(st, root):
#         while root:
#             st.append(root)
#             root = root.right
#
#     def nextLeft(st):
#         node = st.pop()
#         pushLeft(st, node.right)
#         return node.val
#
#     def nextRight(st):
#         node = st.pop()
#         pushRight(st, node.left)
#         return node.val
#
#     stLeft, stRight = [], []
#     pushLeft(stLeft, root)
#     pushRight(stRight, root)
#
#     left, right = nextLeft(stLeft), nextRight(stRight)
#     while left < right:
#         if left + right == k: return True
#         if left + right < k:
#             left = nextLeft(stLeft)
#         else:
#             right = nextRight(stRight)
#     return False

# Solution 3 - Using BST iterator and Python's yield
def findTarget(root, k: int) -> bool:
    def inOrder(root):
        if root:
            yield from inOrder(root.left)
            yield root.val
            yield from inOrder(root.right)

    def inOrderReversed(root):
        if root:
            yield from inOrderReversed(root.right)
            yield root.val
            yield from inOrderReversed(root.left)

    leftGenerator = inOrder(root)
    rightGenerator = inOrderReversed(root)

    left, right = next(leftGenerator), next(rightGenerator)
    while left < right:
        if left + right == k: return True
        if left + right < k:
            left = next(leftGenerator)
        else:
            right = next(rightGenerator)
    return False

print(findTarget([5,3,6,2,4,None,7], 9))