import unittest
from project.models.board import Board


class TestBoardNextGrind(unittest.TestCase):
    def setUp(self):
        size = 3
        self.board = Board(size, size)

    def test_board_calcul_1(self):
        self.board.set_initial_grid(([0, 0],[1, 0],[0, 1],))
        self.board.next_grid()

        true_position = [[0, 0],[1, 0],[0, 1], [1, 1]]
        self.__test_true_position(true_position)


    def __test_true_position(self, true_position: list) -> None:
        for x in range(self.board.width):
            for y in range(self.board.height):
                self.assertEqual(self.board.grid[x][y].state, [x, y] in true_position)

if __name__ == '__main__':
    unittest.main()