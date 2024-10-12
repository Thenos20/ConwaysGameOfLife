import tkinter as tk

class GridGUI:
    def __init__(self, master, grid):
        self.master = master
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.buttons = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        self.create_widgets()

    def create_widgets(self):
        for i in range(self.rows):
            for j in range(self.cols):
                color = 'white' if self.grid[i][j] == 0 else 'black'
                button = tk.Button(self.master, bg=color, width=2, height=1,
                                   command=lambda i=i, j=j: self.toggle_color(i, j))
                button.grid(row=i, column=j, padx=1, pady=1)
                self.buttons[i][j] = button

    """def toggle_color(self, i, j):
        current_color = self.buttons[i][j].cget('bg')
        new_color = 'white' if current_color == 'black' else 'black'
        self.buttons[i][j].config(bg=new_color)"""

    def toggle_color(self, i, j):
        current_color = self.buttons[i][j].cget('bg')
        new_color = 'white' if current_color == 'black' else 'black'
        self.buttons[i][j].config(bg=new_color)

        # Update the grid based on the new color
        self.grid[i][j] = 1 if new_color == 'black' else 0

    def update_grid(self, new_grid):
        self.grid = new_grid
        for i in range(self.rows):
            for j in range(self.cols):
                color = 'white' if self.grid[i][j] == 0 else 'black'
                self.buttons[i][j].config(bg=color)

    def get_grid(self):
        """Returns the current state of the grid."""
        return self.grid