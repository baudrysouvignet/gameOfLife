from project.models.cells import Cells


class Board:
    DIMENSION_TYPE_ERROR_MSG = "Height and width must be integers"

    INITIAL_POSITION_OUT_OF_RANGE = "Position out of range"
    INITIAL_COORDINATE_DATA_ERROR = "The coordinates entered do not match the expected format"

    CALCUL_NEIGHBOURS_CELL_TYPE_ERROR_MSG = "The 'cell' argument must be of type 'Cells'"

    def __init__(self, height: int, width: int)-> None:
        if not all(isinstance(x, int) for x in (height, width)):
            raise ValueError(Board.DIMENSION_TYPE_ERROR_MSG)

        self.grid = [[Cells(x, y) for x in range(width)]for y in range(height)]
        self.width, self.height = width, height

    def set_initial_grid(self, positions: tuple)-> None:
        if not isinstance(positions, tuple) or not all(
            isinstance(pos, list) and len(pos) == 2 and all(isinstance(coordinate, int) for coordinate in pos)
            for pos in positions
        ):
            raise ValueError(Board.INITIAL_COORDINATE_DATA_ERROR)

        for coordinate in positions:
            if self.width > coordinate[0] >= 0 and self.height > coordinate[1] >= 0:
                self.grid[coordinate[0]][coordinate[1]].set_state(True)
            else:
                raise ValueError(Board.INITIAL_POSITION_OUT_OF_RANGE)

    def __calcul_neighbours(self, cell: Cells) -> int:
        if not isinstance(cell, Cells):
            raise ValueError(Board.CALCUL_NEIGHBOURS_CELL_TYPE_ERROR_MSG)

        neighbours = [
            (x, y)
            for x in range(cell.x-1, cell.x+2)
            for y in range(cell.y -1, cell.y+2)
            if (x, y) != (cell.x, cell.y) and 0 <= x < self.width and 0 <= y < self.height
        ]

        return sum(self.grid[pos[0]][pos[1]].state for pos in neighbours)

    def next_grid(self) -> None:
        new_grid = [[Cells(x, y) for x in range(self.width)]for y in range(self.height)]

        for x in range(self.width):
            for y in range(self.height):
                neighbours = self.__calcul_neighbours(self.grid[x][y])
                if self.grid[x][y].state :
                    new_grid[x][y].set_state(neighbours in [2, 3])
                else:
                    new_grid[x][y].set_state(neighbours == 3)

        self.grid = new_grid