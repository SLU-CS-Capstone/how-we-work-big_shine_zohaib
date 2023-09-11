from maze import Maze

#ZOHABIBI 
sizeOfMaze = int(input("Please select a size for your maze: "))
maze = Maze(sizeOfMaze)
maze.generate_maze()
maze.print()
print("Welcome to 2D maze")
