import random
from Gameoflife import nextGeneration, generate_random_grid, Game, create_empty_matrix
from GUI import GridGUI
import tkinter as tk


M,N,gens = 10,10,10

grid_ = generate_random_grid(20, 20)
grid__ = [
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
grid = create_empty_matrix(button_width=20, button_height=20)
print("original grid")
for i in range(M):
    for j in range(N):

        if(grid[i][j] == 0):
            print(".", end="")
        else:
            print("*", end="")
    print()
print()




if __name__ == "__main__":
    root1 = tk.Tk()
    root1.title("Choose grid")
    app1 = GridGUI(root1, grid__)
    root1.mainloop()
    chosengrid = app1.get_grid()

    root = tk.Tk()
    root.title("Grid from Matrix")
    app = GridGUI(root, chosengrid)
    Game(chosengrid,app,root)
    root.mainloop()

