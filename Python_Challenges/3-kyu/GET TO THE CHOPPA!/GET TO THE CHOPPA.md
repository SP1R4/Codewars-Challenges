# 🗺️ GET TO THE CHOPPA

This code provides a function `GET TO THE CHOPPA` that finds the shortest path in a grid of nodes from a starting node to an ending node. If no path exists, it returns an empty list.

## Problem Description
For this kata you must create a function that will find the shortest possible path between two nodes in a 2D grid of nodes.

Details:

- Your function will take three arguments: a grid of nodes, a start node, and an end node. Your function will return a list of nodes that represent, in order, the path that one must follow to get from the start node to the end node. The path must begin with the start node and end with the end node. No single node should be repeated in the path (ie. no backtracking).

```
def find_shortest_path(grid, start_node, end_node):
    pass
```

- The grid is a list of lists of nodes. Each node object has a position that indicates where in the grid the node is (it's indices).

```
node.position.x  # 2
node.position.y  # 5
node.position  # (2,5)
node is grid[2][5]  # True
```

- Each node may or may not be 'passable'. All nodes in a path must be passable. A node that is not passable is effectively a wall that the shortest path must go around.

```
a_node.passable  # True
```

- Diagonal traversals between nodes are NOT allowed in this kata. Your path must move in one of 4 directions at any given step along the path: left, right, up, or down.
- Grids will always be rectangular (NxM), but they may or may not be square (NxN).
- Your function must return a shortest path for grid widths and heights ranging between 0 and 200. This includes 0x0 and 200x200 grids.
- 0x0 grids should return an empty path list
- When more than one shortest path exists (different paths, all viable, with the same number of steps) then any one of these paths will be considered a correct answer.
- Your function must be efficient enough (in terms of time complexity) to pass all the included tests within the allowed timeframe (6 seconds).
- In python, for your convenience, a print_grid function exists that you can use to print a grid. You can also use print_grid to visualize a given path on the given grid. The print_grid function has the following signature:

```
def print_grid(grid, start_node=None, end_node=None, path=None)
# output without a path
"""
S0110
01000
01010
00010
0001E
"""

# output with a path
"""
S0110
#1###
#1#1#
###1#
0001E
"""
```

## 📜 Code Implementation

```python
from preloaded import Node, print_grid
from collections import deque

def find_shortest_path(grid: list[list[Node]], start_node: Node, end_node: Node):
    if not grid or not grid[0]:
        return []
    
    rows, cols = len(grid), len(grid[0])
    
    def neighbors(node):
        x, y = node.position.x, node.position.y
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny].passable:
                yield grid[nx][ny]
    
    start = start_node.position
    end = end_node.position
    
    queue = deque([(start_node, [start_node])])
    visited = set([(start.x, start.y)])
    
    while queue:
        current, path = queue.popleft()
        
        if current.position == end:
            return path
        
        for neighbor in neighbors(current):
            neighbor_pos = (neighbor.position.x, neighbor.position.y)
            if neighbor_pos not in visited:
                visited.add(neighbor_pos)
                queue.append((neighbor, path + [neighbor]))
    
    return []
```

## 🛠️ Explanation

1. **Initialization**: Check if the grid is valid and initialize parameters including grid size and starting/ending nodes.

2. **Neighbors Function**: Generate the neighboring nodes of the current node that are within grid bounds and passable.

3. **Breadth-First Search**: Use a queue to explore the grid level by level. Keep track of visited nodes to avoid cycles.

4. **Path Construction**: If the end node is reached, return the path. Otherwise, continue until all possibilities are explored.

5. **Return Result**: If a path is found, return it; otherwise, return an empty list if no path exists.
