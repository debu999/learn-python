import itertools
from collections import deque


def rotten_apples(grid):
    empty_cells = sum(
        grid[i][j] == 0
        for i, j in itertools.product(range(len(grid)), range(len(grid[0])))
    )
    if empty_cells == len(grid) * len(grid[0]):
        return -2

    # Define the directions for adjacent cells
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Initialize a queue to store the rotten apples
    queue = deque()

    # Initialize the number of days
    days = 0

    # Add the initial rotten apples to the queue and count the fresh apples
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 2:
                queue.append((i, j, days))

    # Perform BFS to rot the fresh apples
    while queue:
        # Get the number of rotten apples at the current day
        rotten_apples_count = len(queue)

        # Process all the rotten apples at the current day
        for _ in range(rotten_apples_count):
            x, y, days = queue.popleft()

            # Check the adjacent cells
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                # Check if the adjacent cell is within the grid and contains a fresh apple
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1:
                    # Mark the adjacent apple as rotten
                    grid[nx][ny] = 2
                    # Add the rotten apple to the queue
                    queue.append((nx, ny, days + 1))

    # Count the number of fresh apples
    fresh_apples = sum(
        grid[i][j] == 1
        for i, j in itertools.product(range(len(grid)), range(len(grid[0])))
    )
    # Check if there are any remaining fresh apples
    return -1 if fresh_apples else days


if __name__ == "__main__":
    print(rotten_apples([[1, 2, 1, 1]]))
