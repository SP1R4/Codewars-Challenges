def tree_by_levels(root):
    if root is None:
        return []

    result = []
    queue = [root]
    
    while queue:
        current = queue.pop(0)
        result.append(current.value)
        
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)
    
    return result