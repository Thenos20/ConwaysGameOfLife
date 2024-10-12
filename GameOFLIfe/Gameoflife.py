import random
from GUI import GridGUI
import time
#function to print next gen
def nextGeneration(grid):

    M = len(grid)
    N = len(grid[0]) if M > 0 else 0

    future = [[0 for i in range(N)] for j in range(M)]

    for l in range(M):
        for m in range(N):
            aliveNeighbours = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if((l+i>=0 and l+i<M) and (m+j>=0 and m+j<N)):
                        aliveNeighbours += grid[l+i][m+j]

            aliveNeighbours -= grid[l][m]

            """if(grid[l][m]==1 and aliveNeighbours<2):
                future[l][m] = 0
            elif(grid[l][m] ==1 and aliveNeighbours>2):
                future[l][m] = 0
            elif(grid[l][m]==0 and aliveNeighbours==3):
                future[l][m] = 1
            else:
                future[l][m] = grid[l][m]"""

            # Cell is lonely and dies
            if ((grid[l][m] == 1) and (aliveNeighbours < 2)):
                future[l][m] = 0

            # Cell dies due to overpopulation
            elif ((grid[l][m] == 1) and (aliveNeighbours > 3)):
                future[l][m] = 0

            # A new cell is born
            elif ((grid[l][m] == 0) and (aliveNeighbours == 3)):
                future[l][m] = 1

            # Cell survives with 2 or 3 alive neighbors
            elif ((grid[l][m] == 1) and (aliveNeighbours == 2 or aliveNeighbours == 3)):
                future[l][m] = 1  # Ensure cell remains alive

            # Remains the same
            else:
                future[l][m] = grid[l][m]

    print("Next generation ")

    for i in range(M):
        for j in range(N):
            if(future[i][j] == 0):
                print(".",end="")
            else:
                print("*", end="")
        print()



    grid[:] = future
    return grid

#generates random grid
def generate_random_grid(rows, cols):
    grid = [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]
    return grid

def create_empty_matrix(button_width=20, button_height=20):
    # Define Full HD screen dimensions
    screen_width = 1920
    screen_height = 1080

    # Calculate the number of columns and rows based on button sizes
    num_columns = screen_width // button_width  # Number of columns
    num_rows = screen_height // button_height    # Number of rows

    # Create an empty matrix (list of lists)
    empty_matrix = [[0 for _ in range(num_columns)] for _ in range(num_rows)]

    return empty_matrix

def Game(grid, gui, root):
    new_grid = nextGeneration(grid)  # Get the next generation
    gui.update_grid(new_grid)  # Update the GUI with the new grid
    grid[:] = new_grid  # Update the underlying grid
    root.after(500, Game, grid, gui, root)



