# **Pacman Game Project**

This is a Python-based implementation of a Pacman-like game using the Pygame library. The game includes dynamic maze generation, ghost behaviors, and win conditions similar to the original Pacman game. The player controls Pacman, who must navigate the maze, avoid ghosts, and collect all pellets (points) to win the game. The difficulty of the game increases over time as the maze becomes more complex, and the ghosts move faster.


## **Features**
- **Dynamic Maze Generation**: The maze is generated randomly using a Depth-First Search (DFS) algorithm that ensures no dead-ends. Each maze is unique and fully navigable without isolated regions.
- **Ghosts with Multiple Behaviors**:
  - Aggressive ghost: Always chases Pacman using the A* algorithm.
  - Random ghost: Moves in random directions.
  - Cautious ghost: Uses a combination of BFS and random movement to avoid or chase Pacman depending on proximity.
- **Difficulty Scaling**: As the game progresses, the speed of the ghosts increases and the complexity of the maze increases.
- **Win Condition**: Pacman must collect all the pellets scattered around the maze to win the game.
- **Game Over Condition**: If a ghost catches Pacman, the game ends with a loss.

## **Game Mechanics**
1. **Dynamic Maze**: The maze is generated dynamically at the start of each level using a recursive DFS algorithm, ensuring no dead-ends and multiple paths for Pacman and ghosts to navigate.
2. **Pellets**: Each open cell in the maze contains a pellet that Pacman must collect. The game ends when all pellets are collected.
3. **Ghost Behavior**:
   - **Aggressive**: Chases Pacman using the shortest path (A*).
   - **Random**: Moves unpredictably through the maze.
   - **Cautious**: Avoids Pacman if close, but otherwise chases Pacman.
4. **Difficulty Scaling**: Ghosts' speed increases as the game progresses, and the maze complexity increases with each level.

## **Installation**
To install and run the game, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/MykhailoTanchuk/pacman.git
    cd pacman-game
    ```

2. **Install dependencies**:
    Ensure you have Python 3.x installed. You can install the required dependencies using:
    ```bash
    pip install pygame
    ```

3. **Run the game**:
    ```bash
    python main.py
    ```

## **How to Play**
1. **Objective**: Navigate Pacman through the maze and collect all the pellets while avoiding the ghosts.
2. **Controls**:
   - Use the arrow keys to move Pacman up, down, left, or right.
   - Pacman can only move one cell at a time and must stay within the maze's bounds.
3. **Winning**: Collect all the pellets on the screen to complete the level.
4. **Losing**: If a ghost catches Pacman, the game is over.

## **Files Overview**
- **`main.py`**: The entry point of the game. Handles the game loop, updates game state, and checks for win/lose conditions.
- **`maze.py`**: Contains the Maze class for generating a dynamic, DFS-based maze and handling pellet logic.
- **`pacman.py`**: Contains the Pacman class, handling movement and interaction with the maze.
- **`ghost.py`**: Contains the Ghost class and its behaviors (aggressive, random, cautious), along with pathfinding algorithms like A* and BFS.
- **`constants.py`**: Holds constant values for colors, grid sizes, and speeds used throughout the game.

## **Credits**
- **Pygame Library**: This project uses the Pygame library for handling graphics, input, and game loops.
- **Algorithm Resources**: The maze generation logic is based on the classic DFS algorithm, adapted for game use.
- **Your Contributions**: Special thanks to contributors for feedback and suggestions!
