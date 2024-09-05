class Cells:
    def __init__(self, x:int, y:int):
        self.r = x
        self.i = y
        self.state = False

    def set_state(self, state: bool) -> None:
        if not isinstance(state, bool):
            raise ValueError("The state must be a boolean")
        self.state = state