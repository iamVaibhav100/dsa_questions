from collections import deque
def rightSideView(root) -> list[int]:
    if not root:
        return []
    ans = []
    curr = deque([root])
    while curr:
        val = None

        for i in range(len(curr)):
            popped = curr.popleft()
            val = popped.val
            if popped.left:
                curr.append(popped.left)
            if popped.right:
                curr.append(popped.right)
        ans.append(val)
    return ans

print(rightSideView([1,2,3,None,5,None,4]))