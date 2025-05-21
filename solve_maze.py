# Ahmad Ughurluzada 211ADB063
# This solution finds the shortest path from S to G in a maze,
# and among equally short paths, chooses the one with the smallest coin sum.

import sys
import heapq


def solve_maze_file(filepath):
    """
    Here we analyze a maze file and compute coin-minimal path among all shortest paths
    from the start S to the goal G. It supports 8 directional movement.

    :param filepath: Path to the text file that contains the maze  
    :return:  Sum of coins collected on the chosen path. If no path exists, it becomes None
    """
    # Read and clean the input grid
    grid = []
    with open(filepath, 'r') as file:
        for raw_line in file:
            line = raw_line.rstrip("\n")
            if line:  # skip blank lines
                grid.append(list(line))

    rows = len(grid)
    cols = len(grid[0])

    # Find positions of start S and goal G
    start = goal = None
    for r in range(rows):
        for c in range(cols):
            cell = grid[r][c]
            if cell == 'S':
                start = (r, c)
            elif cell == 'G':
                goal = (r, c)

    if start is None or goal is None:
        raise ValueError("Maze must contain one S and one G")

    # Define the 8 possible moves: north, south, east, west, and four diagonals
    directions = [(-1,  0), (1,  0), (0, -1), (0,  1),
                  (-1, -1), (-1, 1), (1, -1), (1,  1)]

    # Initialize distance and coin-tracking grids
    INF = float('inf')
    # distance_grid[r][c] = fewest steps to reach cell (r, c)
    distance_grid = [[INF] * cols for _ in range(rows)]
    # coin_grid[r][c] = fewest coins collected on any shortest path to (r, c)
    coin_grid     = [[INF] * cols for _ in range(rows)]

    # We start at S with 0 steps and 0 coins
    sr, sc = start
    distance_grid[sr][sc] = 0
    coin_grid[sr][sc]     = 0

    # Priority queue holds tuples: (steps, coins, row, col)
    pq = [(0, 0, sr, sc)]

    while pq:
        steps, coins, r, c = heapq.heappop(pq)

        # If this entry is outdated compared to our best-known values, skip it
        if steps > distance_grid[r][c] or (steps == distance_grid[r][c] and coins > coin_grid[r][c]):
            continue

        # If we've reached the goal, we can return the coin sum
        if (r, c) == goal:
            return coins

        # Explore each neighbor cell
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            # Check bounds and collision with wall
            if not (0 <= nr < rows and 0 <= nc < cols):
                continue  # outside maze is lava
            if grid[nr][nc] == 'X':
                continue  # wall, impossible to pass

            # define coin value at the neighbor (digits only, S/G count as zero)
            char = grid[nr][nc]
            add_coins = int(char) if char.isdigit() else 0

            new_steps = steps + 1
            new_coins = coins + add_coins

            # If this path is strictly better (fewer steps or same steps + fewer coins)
            if (new_steps < distance_grid[nr][nc] or
               (new_steps == distance_grid[nr][nc] and new_coins < coin_grid[nr][nc])):
                # Record improvements
                distance_grid[nr][nc] = new_steps
                coin_grid[nr][nc]     = new_coins
                # Push into the queue for further exploration
                heapq.heappush(pq, (new_steps, new_coins, nr, nc))

    # If queue empties without reaching G, there's no valid path
    return None


def main():
    """
    Entry point: expects one or more maze filenames on the command line.
    Prints a comma-separated list of coin sums for each maze in order.
    """
    if len(sys.argv) < 2:
        print("Usage: python solve_maze.py <maze1.txt> [<maze2.txt> ...]")
        sys.exit(1)

    results = []
    for maze_file in sys.argv[1:]:
        try:
            coin_total = solve_maze_file(maze_file)
        except Exception as e:
            print(f"Error processing {maze_file}: {e}")
            sys.exit(1)

        if coin_total is None:
            print(f"No path found for {maze_file}")
            sys.exit(1)

        results.append(str(coin_total))

    # To output all results in one line, comma-separated
    print(",".join(results))


if __name__ == '__main__':
    main()