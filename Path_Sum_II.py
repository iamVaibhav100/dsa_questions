def pathSum(root, targetSum):

    def dfs(node, targetSum, node_list):
        if not node:
            return

        targetSum -= node.val
        node_list.append(node.val)

        if not node.left and not node.right:
            if targetSum == 0:
                ans.append(node_list.copy())

        else:
            dfs(node.left, targetSum, node_list)
            dfs(node.right, targetSum, node_list)

        node_list.pop()

    ans = []
    dfs(root, targetSum, [])
    return ans