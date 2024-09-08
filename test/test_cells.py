import unittest
from project.models.cells import Cells

class TestCells(unittest.TestCase):
    def setUp(self):
        self.cell = Cells(1, 2)

    def test_cell_declaration_invalid(self):
        with self.assertRaises(ValueError) as context:
            Cells('1', '2')

        self.assertEqual(str(context.exception), Cells.COORDINATE_TYPE_ERROR_MSG)

    def test_set_state_true(self):
        self.cell.set_state(True)
        self.assertTrue(self.cell.state)


    def test_set_state_false(self):
        self.cell.set_state(False)
        self.assertFalse(self.cell.state)


    def test_set_state_invalid(self):
        with self.assertRaises(ValueError) as context:
            self.cell.set_state("invalid")

        self.assertEqual(str(context.exception), Cells.STATE_TYPE_ERROR_MSG)

if __name__ == '__main__':
    unittest.main()