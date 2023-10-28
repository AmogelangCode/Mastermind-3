import unittest
import patterns
from io import StringIO
from unittest.mock import patch

class TestPatterns(unittest.TestCase):
    """ mocks shape input and checks if shape is valid"""    
    @patch("patterns.get_shape")
    def test_get_shape(self, mock_shape):
        shapes = ["square","triangle","pyramid"]
        y = "-".join(shapes)
        mock_shape.return_value = "square"
        self.assertTrue(y.find(patterns.get_shape()) != -1)

    # somehow this block of code runs the patterns python file instead of the test file
    # @patch("patterns.get_shape")
    # def test_2_get_shape(self, mock_shape):
    #     mock_shape.return_value = "pyramid"
    #     self.assertTrue(patterns.get_height().islower())
    
    """mocks height and checks if height is a number and has a maximum of 80"""
    @patch("patterns.get_height")
    def test_get_height(self, mock_height):
        mock_height.return_value = 5
        self.assertEqual(type(patterns.get_height()), int)
        self.assertTrue(patterns.get_height() <= 80)

    """mock height to use it as the argument """
    @patch("patterns.get_height") 
    def test_draw_square(self, mock_height):
        mock_height.return_value = 3 
        output = "***\n***\n***"
        
        """"redirects the print output of draw_square to become mock output"""
        with patch("sys.stdout", new_callable=StringIO) as mock_output:
            patterns.draw_square(mock_height())
            self.assertEqual(mock_output.getvalue().strip(), output)

    """mocks height to use it as the argument """
    @patch("patterns.get_height")
    def test_draw_triangle_reversed(self, mock_height):
        mock_height.return_value = 3
        output = "1 1 1 \n2 2 \n3"
        
        """"redirects the print output of draw_triangle reversed to become mock output"""
        with patch("sys.stdout", new_callable=StringIO) as mock_output:
            patterns.draw_triangle_reversed(mock_height())
            self.assertEqual(mock_output.getvalue().strip(), output)

    """mocks height to use it as the argument """
    @patch("patterns.get_height") 
    def test_draw_triangle(self, mock_height):
        mock_height.return_value = 3
        output = "1 \n1 2 \n1 2 3"
        
        """"redirects the print output of draw_triangle reversed to become mock output"""
        with patch("sys.stdout", new_callable=StringIO) as mock_output:
            patterns.draw_triangle(mock_height())
            self.assertEqual(mock_output.getvalue().strip(), output)

    
    """mocks height to use it as the argument """
    @patch("patterns.get_height") 
    def test_draw_triangle(self, mock_height):
        mock_height.return_value = 3
        output = "1 \n1 2 \n1 2 3"
        
        """"redirects the print output of draw_triangle to become mock output"""
        with patch("sys.stdout", new_callable=StringIO) as mock_output:
            patterns.draw_triangle(mock_height())
            self.assertEqual(mock_output.getvalue().strip(), output)

    """mocks height to use it as the argument """
    @patch("patterns.get_height") 
    def test_draw_triangle_prime(self, mock_height):
        mock_height.return_value = 5
        output = "2 \n3 5 \n7 11 13 \n17 19 23 29 \n31 37 41 43 47"
        
        """"redirects the print output of draw triangle prime to become mock output"""
        with patch("sys.stdout", new_callable=StringIO) as mock_output:
            patterns.draw_triangle_prime(mock_height())
            self.assertEqual(mock_output.getvalue().strip(), output)
    








if __name__=="__main__":
    unittest.main()