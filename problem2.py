""" Problem Statement:
We are given a grid where zombies (denoted by 1) can infect adjacent cells (up, down, left, right). The task is to determine the number of days it will take for all cells to be infected or return -1 if it’s not possible.

Approach:
This is a Breadth-First Search (BFS) problem where we start from all zombie cells simultaneously and spread out. BFS ensures that we visit cells level-by-level, where each level represents one day.
    """
    
from collections import deque

def min_days_to_infect(grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    empty_cells = 0  # Count empty cells to check if all get infected

    # Step 1: Initialize the queue with all initial zombie positions
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:  # Zombie cell
                queue.append((r, c, 0))  # (row, col, days)
            elif grid[r][c] == 0:  # Empty cell
                empty_cells += 1
    
    if empty_cells == 0:
        return 0  # No cells to infect
    
    # Step 2: BFS to spread infection
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Directions: right, down, left, up
    max_days = 0
    
    while queue:
        r, c, days = queue.popleft()
        max_days = max(max_days, days)
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                grid[nr][nc] = 1  # Infect the cell
                queue.append((nr, nc, days + 1))
                empty_cells -= 1
    
    return max_days if empty_cells == 0 else -1

# Example input
grid = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 0]
]
print(min_days_to_infect(grid))
