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

    def count_neighbors(self, row, col):
        # Keeps track of how many living cells surround this cell.
        count = 0

        # Check all eight cells surrounding the current cell.
        for row_offset in [-1, 0, 1]:
            for col_offset in [-1, 0, 1]:

                # Skip the current cell
                if row_offset == 0 and col_offset == 0:
                    continue

                neighbor_row = row + row_offset
                neighbor_col = col + col_offset

                # Making sure the neighbor is inside the game board.
                if (
                    0 <= neighbor_row < self.height and 0 <= neighbor_col < self.width
                ):
                    if self.grid[neighbor_row][neighbor_col]:
                        count += 1

        return count

    def next_generation(self):
        # Creates a new grid for the next generation.
        new_grid = [
            [False for _ in range(self.width)]
            for _ in range(self.height)
        ]

        # Checks every cell on the current grid.
        for row in range(self.height):
            for col in range(self.width):
                neighbors = self.count_neighbors(row, col)

                # Apply the game of life rules.
                if self.grid[row][col]:
                    # A living cell survives with 2 or 3 neighbors.
                    if neighbors == 2 or neighbors == 3:
                        new_grid[row][col] = True
                else:
                    # A dead cell becomes alive with exactly 3 neighbors.
                    if neighbors == 3:
                        new_grid[row][col] = True

        # Replace the current grid with the new generation.
        self.grid = new_grid