from project.models.board import Board

grille = Board(3, 3)
grille.set_initial_grid(([0,0], [0,1],[1,0],))

print(grille.grid[1][1].state)

grille.next_grid()


print(grille.grid[0][0].state)
print(grille.grid[1][2].state)
print(grille.grid[1][1].state)