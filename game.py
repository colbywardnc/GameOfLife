class GameOfLife:
    def __init__(self, width, height):
        # Store the size of the game board.
        self.width = width
        self.height = height

        # Creates a grid where False represents a dead cell
        # and True is a living cell.
        self.grid = [
            [False for _ in range(width)]
            for _ in range(height)
        ]