class Cells:
    COORDINATE_TYPE_ERROR_MSG = "The cell coordinates must be a integers"
    STATE_TYPE_ERROR_MSG = "The state must be a boolean"

    def __init__(self, x:int, y:int,):
        if not all(isinstance(x, int) for x in (x, y)):
            raise ValueError(Cells.COORDINATE_TYPE_ERROR_MSG)
        self.r = x
        self.i = y
        self.state = False

    def set_state(self, state: bool) -> None:
        if not isinstance(state, bool):
            raise ValueError(Cells.STATE_TYPE_ERROR_MSG)
        self.state = state