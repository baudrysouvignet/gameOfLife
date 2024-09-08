import unittest
from project.models.board import Board

class TestCells(unittest.TestCase):
    def setUp(self):
        self.cell = Board(10, 10)

    def test_cell_declaration_invalid(self):
        with self.assertRaises(ValueError) as context:
            Board('1', '2')

        self.assertEqual(str(context.exception), Board.DIMENSION_TYPE_ERROR_MSG)

if __name__ == '__main__':
    unittest.main()