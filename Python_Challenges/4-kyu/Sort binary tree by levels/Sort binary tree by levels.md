# 🌳 Sort Binary Tree

This repository includes a solution for traversing a binary tree by levels. The `Sort Binary Tree` function returns a list of values representing the tree nodes in level-order traversal.

## 📝 Problem Description

You are given a binary tree:
```
class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n
```
Your task is to return the list with elements from tree sorted by levels, which means the root element goes first, then root children (from left to right) are second and third, and so on.

Return empty list if root is None.

Example 1 - following tree:




```
                 2
            8        9
          1  3     4   5
```

Should return following list:

```
[2,8,9,1,3,4,5]
```

## 💡 Solution

The solution uses a breadth-first search (BFS) approach with a queue to traverse the tree level by level. Nodes are visited and their values are collected in the order they are encountered.

### Approach

1. **Initialize Queue**:
   - Start with the root node in the queue.

2. **Process Each Node**:
   - Remove nodes from the queue one by one, append their values to the result list.
   - Add the left and right children of each node to the queue if they exist.

3. **Return Result**:
   - After processing all nodes, return the list of values.

### Code Implementation

```python
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
```

### How It Works

- **Queue Initialization**:
  - The `queue` starts with the root node. It helps in keeping track of nodes to be processed.

- **Node Processing**:
  - Nodes are processed level by level. For each node, its value is added to the result list, and its children (if any) are added to the queue.

- **Completion**:
  - The traversal continues until the queue is empty, ensuring all nodes are processed.
