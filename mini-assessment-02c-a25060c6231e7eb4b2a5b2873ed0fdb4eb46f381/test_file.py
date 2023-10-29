import unittest
from io import StringIO
import sys
from unittest.mock import patch
import patterns

class TestgetShape(unittest.TestCase):

    @patch('builtins.input', side_effect=["circle", "square"])
    def test_get_shape_invalid_then_valid(self, mock_input):
        # First, we provide an invalid shape ("circle"), and then a valid one ("square").
        self.assertEqual(patterns.get_shape(), "square")

    @patch('builtins.input', side_effect=["triangle"])
    def test_get_shape_valid(self, mock_input):
        # Provide a valid shape ("triangle").
        self.assertEqual(patterns.get_shape(), "triangle")
        
    
class TestGetHeight(unittest.TestCase):

    @patch('builtins.input', side_effect=["abc", "0", "-7", "15"])
    def test_get_height_invalid_then_valid(self, mock_input):
        # Test with invalid inputs followed by a valid input.
        self.assertEqual(patterns.get_height(), 20) 
        
        
class TestDrawSquare(unittest.TestCase):

    def setUp(self):
        self.output = StringIO()
        sys.stdout = self.output

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_draw_square(self):
        patterns.draw_square(5)
        expected_output = (
            "*****\n"
            " ****\n"
            "  ***\n"
            "   **\n"
            "    *\n"
        )
        self.assertEqual(self.output.getvalue(), expected_output)
        
        
def test_tower_of_hanoi_3_disks(self):
        n = 3
        source_peg = "A"
        auxiliary_peg = "B"
        target_peg = "C"

        moves = patterns.tower_of_hanoi(n, source_peg, auxiliary_peg, target_peg)

        expected_moves = [
            ("A", "C"),
            ("A", "B"),
            ("C", "B"),
            ("A", "C"),
            ("B", "A"),
            ("B", "C"),
            ("A", "C"),
        ]

        self.assertEqual(moves, expected_moves)        
        
    


if __name__ == '__main__':
    unittest.main()