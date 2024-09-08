from project.models.board import Board

grille = Board(4, 4)
grille.set_initial_grid(([0,0], [2,2],))
grille.calcul_neighbours(grille.grid[1][1])
grille.calcul_neighbours(grille.grid[1][1])
print(grille.grid[0][0].state, grille.grid[1][1].state)