from game import GameOfLife

game = GameOfLife(5, 5)

game.grid[1][2] = True
game.grid[2][2] = True
game.grid[3][2] = True

print("Before:")
for row in game.grid:
    print(row)

game.next_generation()

print("\nAfter:")
for row in game.grid:
    print(row)