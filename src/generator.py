from maze import Maze


sizeOfMaze = int(input("Welcome to 2D Maze! Please select a size for your maze: "))
maze = Maze(sizeOfMaze)
maze.generate_maze()
maze.print()
print("Welcome to 2D maze")
