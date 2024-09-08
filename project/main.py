
from project.models.board import Board

grille = Board(4, 4)
grille.set_initial_grid([[0,0], [3,3]])
print(grille.grid[1][2].state, grille.grid[1][1].state)