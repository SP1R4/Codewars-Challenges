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