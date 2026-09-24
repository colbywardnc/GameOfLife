import tkinter as tk

from game import GameOfLife

class GameOfLifeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Game of Life")

        self.game = GameOfLife(20, 20)

        self.canvas = tk.Canvas(
            root,
            width=500,
            height=500,
        )
        self.canvas.pack()

        self.step_button = tk.Button(
            root,
            text="Step",
            command=self.step
        )
        self.step_button.pack()

        self.reset_button = tk.Button(
            root,
            text="Reset",
            command=self.reset
        )
        self.reset_button.pack()

        self.canvas.bind("<Button-1>", self.toggle_cell)

        self.draw_grid()

    def draw_grid(self):
        self.canvas.delete("all")

        cell_width = 500 / self.game.width
        cell_height = 500 / self.game.height

        for row in range(self.game.height):
            for col in range(self.game.width):
                x1 = col * cell_width
                y1 = row * cell_height
                x2 = x1 + cell_width
                y2 = y1 + cell_height

                self.canvas.create_rectangle(
                    x1,
                    y1,
                    x2,
                    y2,
                    fill="black" if self.game.grid[row][col] else "white",
                    outline="grey"
                )

    def toggle_cell(self, event):
        # Find the row and col of the cell that was clicked
        cell_width = 500 / self.game.width
        cell_height = 500 / self.game.height

        col = int(event.x / cell_width)
        row = int(event.y / cell_height)

        # Toggle the cell between alive and dead
        self.game.grid[row][col] = not self.game.grid[row][col]

        # Redraw the grid to show the change.
        self.draw_grid()

    def step(self):
        # Move the game forward by one generation
        self.game.next_generation()

        # Update the grid to show the new generation
        self.draw_grid()

    def reset(self):
        # Create a new empty game board
        self.game = GameOfLife(20,20)

        # Update the grid to show the empty board.
        self.draw_grid()

root = tk.Tk()
app = GameOfLifeApp(root)
root.mainloop()