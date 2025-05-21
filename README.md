# Maze Solver

## Description
This Python script, `solve_maze.py`, computes a path through a maze text file by:
1. Finding the **shortest path** (fewest steps) from `S` to `G` with 8-directional moves.
2. Among equally short paths, choosing the one with the **minimum total coins** collected (cells labeled 0–9).

## Requirements
- Python 3.6 or newer
- No external dependencies (uses only the Python standard library)

## Installation & Setup
1. Clone or download this repository (or just place the files) into a folder.  
2. Ensure the following files are present:
   - `solve_maze.py`
   - Your maze text files (e.g., `maze_11x11.txt`, `maze_31x31.txt`, `maze_101x101.txt`).

## Usage
Open a terminal in that folder and run:
```bash
python solve_maze.py maze_11x11.txt maze_31x31.txt maze_101x101.txt
```

The script will print a comma-separated list of coin sums for each maze:
```bash
99,1076,1763
```

## Algorithm & Complexities
 - **Core algorithm:** A lexicographic variant of Dijkstra’s algorithm, where each node’s priority is (steps, coins).

 - **Time Complexity:**
    - **Worst case:** O((R × C) log(R × C)), where R×C is the number of cells, due to priority-queue operations.
    - **Alternative approaches:**
      - BFS + DP: Run BFS to find minimal steps, then dynamic programming to minimize coins on those paths; similar overall bound but with extra constant overhead.
       - A* with a heuristic (e.g., Chebyshev distance) often runs faster in practice, but worst-case still O((R × C) log(R × C)).

 - **Space Complexity:**
O(R × C) for storing the grid, distance and coin arrays, and priority-queue state.
