
def is_same_tree(p, q) -> bool:
    # base case: if both trees are None, they are the same
    if not p and not q:
        return True
    # base case: if only one tree is None, they are not the same
    if not p or not q:
        return False

    # create a queue to hold the nodes at each level
    queue = [(p, q)]

    # do a BFS of the trees
    while queue:
        # get the next nodes to compare
        node1, node2 = queue.pop(0)
        # check if the nodes are the same
        if node1.val != node2.val:
            return False
        # add the left and right children of the nodes to the queue if they exist
        if node1.left and node2.left:
            queue.append((node1.left, node2.left))
        elif node1.left or node2.left:
            # if only one of the nodes has a left child, the trees are not the same
            return False
        if node1.right and node2.right:
            queue.append((node1.right, node2.right))
        elif node1.right or node2.right:
            # if only one of the nodes has a right child, the trees are not the same
            return False
    # if we made it through the loop, the trees are the same
    return True


def is_same_tree_recursive(p, q) -> bool:
    # base case: if both trees are None, they are the same
    if not p and not q:
        return True
    # base case: if only one tree is None, they are not the same
    if not p or not q:
        return False

    # check if the values of the nodes are the same
    if p.val != q.val:
        return False
    # check if the left and right subtrees are the same
    return is_same_tree_recursive(p.left, q.left) and is_same_tree_recursive(p.right, q.right)
