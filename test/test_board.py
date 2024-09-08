import unittest
from project.models.board import Board

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board(10, 10)

    def test_board_declaration_invalid(self):
        with self.assertRaises(ValueError) as context:
            Board('1', '2')

        self.assertEqual(str(context.exception), Board.DIMENSION_TYPE_ERROR_MSG)
    
    def test_board_init(self):
        data = ([0, 0], [0, 1], [1, 0], [1, 1],)
        self.board.set_initial_grid(data)
        self.assertTrue(all(self.board.grid[coordinates[0]][coordinates[1]].state for coordinates in data))

    def test_board_init_out_of_range(self):
        data = ([10, 10],)
        with self.assertRaises(ValueError) as context:
            self.board.set_initial_grid(data)

        self.assertEqual(str(context.exception), self.board.INITIAL_POSITION_OUT_OF_RANGE)
    
    def test_board_init_invalid_type(self):
        data = ([10, '10'],)
        with self.assertRaises(ValueError) as context:
            self.board.set_initial_grid(data)

        self.assertEqual(str(context.exception), self.board.INITIAL_COORDINATE_DATA_ERROR)

    def test_board_init_invalid_structur(self):
        data = ("a", [10, 10, '10'],)
        with self.assertRaises(ValueError) as context:
            self.board.set_initial_grid(data)

        self.assertEqual(str(context.exception), self.board.INITIAL_COORDINATE_DATA_ERROR)

if __name__ == '__main__':
    unittest.main()