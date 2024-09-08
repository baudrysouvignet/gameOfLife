from project.models.cells import Cells


class Board:
    DIMENSION_TYPE_ERROR_MSG = "Height and width must be integers"
    INITIAL_POSITION_OUT_OF_RANGE = "Position out of range"
    INITIAL_COORDINATE_DATA_ERROR = "The coordinates entered do not match the expected format"

    def __init__(self, height: int, width: int)-> None:
        if not all(isinstance(x, int) for x in (height, width)):
            raise ValueError(Board.DIMENSION_TYPE_ERROR_MSG)

        self.grid = [[Cells(x, y) for x in range(height)]for y in range(width)]
        self.width, self.height = width, height

    def set_initial_grid(self, positions: tuple)-> None:
        if not isinstance(positions, tuple) or not all(
            isinstance(pos, list) and len(pos) == 2 and all(isinstance(coordinate, int) for coordinate in pos)
            for pos in positions
        ):
            raise ValueError(Board.INITIAL_COORDINATE_DATA_ERROR)

        for position in positions:
            if self.width > position[0] >= 0 and self.height > position[1] >= 0:
                self.grid[position[0]][position[1]].set_state(True)
            else:
                raise ValueError(Board.INITIAL_POSITION_OUT_OF_RANGE)