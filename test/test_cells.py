import unittest
from project.models.cells import Cells

class TestCells(unittest.TestCase):
    def setUp(self):
        self.cell = Cells(1, 2)

    def test_set_state_true(self):
        self.cell.set_state(True)
        self.assertTrue(self.cell.state)


    def test_set_state_false(self):
        self.cell.set_state(False)
        self.assertFalse(self.cell.state)


    def test_set_state_invalid(self):
        with self.assertRaises(ValueError):
            self.cell.set_state("invalid")

if __name__ == '__main__':
    unittest.main()