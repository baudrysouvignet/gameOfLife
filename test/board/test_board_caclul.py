import unittest
from project.models.board import Board


class TestBoardCalcul(unittest.TestCase):
    def setUp(self):
        self.board = Board(4, 4)

    def test_board_calcul_1(self):
        self.board.set_initial_grid(([0, 0],))
        self.assertEqual(self.board._Board__calcul_neighbours(self.board.grid[1][1]), 1)

    def test_board_calcul_3(self):
        self.board.set_initial_grid(([0, 0],[1, 0],[2, 2],))
        self.assertEqual(self.board._Board__calcul_neighbours(self.board.grid[1][1]), 3)

    def test_board_calcul_2(self):
        self.board.set_initial_grid(([0, 0],[1, 0],[3, 3],))
        self.assertEqual(self.board._Board__calcul_neighbours(self.board.grid[1][1]), 2)

    def test_board_calcul_invalid(self):
        with self.assertRaises(ValueError) as context:
            self.board._Board__calcul_neighbours('invalid')

        self.assertEqual(str(context.exception), self.board.CALCUL_NEIGHBOURS_CELL_TYPE_ERROR_MSG)


if __name__ == '__main__':
    unittest.main()