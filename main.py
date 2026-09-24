import tkinter as tk

from game import GameOfLife

class GameOfLifeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Game of Life")

        self.game = GameOfLife(20, 20)
        self.running = False
        self.generation = 0

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

        self.start_button = tk.Button(
            root,
            text="Start",
            command=self.start
        )
        self.start_button.pack()

        self.pause_button = tk.Button(
            root,
            text="Pause",
            command=self.pause
        )
        self.pause_button.pack()

        self.generation_label = tk.Label(
            root,
            text="Generation: 0"
        )
        self.generation_label.pack()

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
        self.generation += 1

        # Update the grid to show the new generation
        self.draw_grid()

        # Update the generation counter
        self.generation_label.config(
            text="Generation: " + str(self.generation)
        )

    def reset(self):
        # Create a new empty game board
        self.game = GameOfLife(20,20)
        self.generation = 0

        # Update the grid to show the empty board.
        self.draw_grid()
        self.generation_label.config(
            text="Generation: 0"
        )

    def start(self):
        # Start the simulation.
        self.running = True

        # Begin updating the game.
        self.run_game()

    def run_game(self):
        # Only continue running if the sim is active.
        if self.running:
            self.step()

            # Run again after 200 milliseconds
            self.root.after(200, self.run_game)

    def pause(self):
        # Stop the sim from running.
        self.running = False

root = tk.Tk()
app = GameOfLifeApp(root)
root.mainloop()