from io import StringIO
import sys
import unittest
from unittest.mock import patch
from patterns import *

class MyTestCase(unittest.TestCase):
    @patch("builtins.input", side_effect=["circle", "square", "triangle"])
    def test_get_shape(self, mock_input):
        shape = get_shape()
        self.assertEqual(shape, "square")
        shape = get_shape()  
        self.assertEqual(shape, "triangle")

    # def test_get_valid_shape_with_invalid_input_then_valid_input(self, mock_input, mock_stdout):
    #     output = mock_stdout.getvalue()
    #     self.assertIn("Invalid shape. Please enter 'square', 'triangle', or 'pyramid'.", output)
    @patch("builtins.input", side_effect =["6","","99", "two"])
    def test_get_height(self, mock_input):
        height = get_height()
        self.assertTrue(1<= height <= 80)
        self.assertIsInstance(height, int)
    


    @patch("sys.stdout", new_callable=StringIO)
    def test_draw_square(self, mock_stdout):
        expected_output = "****\n****\n****\n****\n"
        with patch("builtins.input", side_effect=["4"]):
            draw_square(4)
            output = mock_stdout.getvalue()
            self.assertEqual(output, expected_output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_draw_triangle(self, mock_stdout):
        expected_output = "$\n$$\n$$$\n$$$$\n"
        with patch("builtins.input", side_effect=["4"]):
            draw_triangle(4)
            output = mock_stdout.getvalue()
            self.assertEqual(output, expected_output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_draw_pyramid(self, mock_stdout):
        expected_output = "    *\n   ***\n  *****\n *******\n*********\n"
        with patch("builtins.input", side_effect=["5"]):
            draw_pyramid(5)
            output = mock_stdout.getvalue()
            self.assertEqual(output, expected_output)

    def test_tower_of_hanoi(self):
        pass

    if __name__ == '__main__':
        unittest.main()
