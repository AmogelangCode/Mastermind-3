import unittest
from io import StringIO
import sys
from unittest.mock import patch
import patterns

class MyTestCase(unittest.TestCase):
    """
    class
    """

    @patch("sys.stdin", StringIO("Square\n"))
    def test_1_shape(self):
        """
        test for valid shape i.e square
        """

        text_capture = StringIO()
        sys.stdout = text_capture
        self.assertEqual(patterns.get_shape(),'square')

    @patch("sys.stdin", StringIO("pYraMid\n"))
    def test_2_shape(self):
        """test for case sensitive valid shape"""

        text_capture = StringIO()
        sys.stdout = text_capture
        self.assertEqual(patterns.get_shape(),'pyramid')

    @patch("sys.stdin", StringIO("5\n"))
    def test_3_height(self):
        """get integer height from user"""

        text_capture = StringIO()
        sys.stdout = text_capture
        self.assertIsInstance(patterns.get_height(),int)

    def test_4_square(self):
        """test drawn square using h=4"""
        
        text_capture = StringIO()
        sys.stdout = text_capture
        patterns.draw_square(4)

        self.assertEqual("""****
****
****
****
""",text_capture.getvalue())

    def test_5_square(self):
        """test drawn square where h =10"""
        
        text_capture = StringIO()
        sys.stdout = text_capture
        patterns.draw_square(10)

        self.assertEqual("""**********
**********
**********
**********
**********
**********
**********
**********
**********
**********
""",text_capture.getvalue())

    def test_6_triangle(self):
        """
        test for reversed triangle with height 0f 3
        """
        with patch("sys.stdout", StringIO("1 1 1 \n2 2 \n3 \n")) as mock_stdout:
            patterns.draw_triangle_reversed(3)
            self.assertEqual(mock_stdout.getvalue(), "1 1 1 \n2 2 \n3 \n")
    

    def test_7_triangle(self):
        """
        test for reversed triangle
        """
        with patch("sys.stdout", StringIO("1 1 1 1 1 \n2 2 2 2 \n3 3 3 \n4 4 \n5 ")) as mock_stdout:
            patterns.draw_triangle_reversed(5)
            self.assertEqual(mock_stdout.getvalue(), "1 1 1 1 1 \n2 2 2 2 \n3 3 3 \n4 4 \n5 \n")


    def test_8_triangle(self):

        """
        test for triangle(right_angled) with height 5
        """
        
        with patch("sys.stdout", StringIO("1 \n1 2 \n1 2 3 \n1 2 3 4 \n1 2 3 4 5")) as mock_stdout:
            patterns.draw_triangle(5)
            self.assertEqual(mock_stdout.getvalue(), "1 \n1 2 \n1 2 3 \n1 2 3 4 \n1 2 3 4 5 \n")

    def test_9_triangle(self):
        """
        test for triangle(right_angled)

        """

        with patch("sys.stdout", StringIO("1 \n1 2 \n1 2 3 \n")) as mock_stdout:
            patterns.draw_triangle(3)
            self.assertEqual(mock_stdout.getvalue(), "1 \n1 2 \n1 2 3 \n")
  

    def test_10_triangle_multiplication(self):
        """
        test for an increamenting multiplication triangle 
        """
        with patch("sys.stdout", StringIO("1 \n2 4 \n3 6 9 \n4 8 12 16 \n")) as mock_stdout:
            patterns.draw_triangle_multiplication(4)
            self.assertEqual(mock_stdout.getvalue(), "1 \n2 4 \n3 6 9 \n4 8 12 16 \n")
        

    def test_11_triangle_multiplication(self):
        """
        test for an increamenting multiplication triangle 
        """

        with patch("sys.stdout", StringIO("1 \n2 4 \n3 6 9 \n4 8 12 16 \n5 10 15 20 25 \n6 12 18 24 30 36 \n")) as mock_stdout:
            patterns.draw_triangle_multiplication(6)
            self.assertEqual(mock_stdout.getvalue(), "1 \n2 4 \n3 6 9 \n4 8 12 16 \n5 10 15 20 25 \n6 12 18 24 30 36 \n")




    def test_12_pyramid(self):
        """
        test for an increamenting multiplication triangle 
        """
        with patch("sys.stdout", StringIO("    * \n   *** \n  ***** \n ******** \n********* \n")) as mock_stdout:
            patterns.draw_pyramid(6)
            self.assertEqual(mock_stdout.getvalue(), "     *\n    ***\n   *****\n  *******\n *********\n***********\n")

    def test_13_pyramid(self):
           """
           test for pyramid
           """
        
           with patch("sys.stdout", StringIO("    * \n   *** \n  ***** \n")) as mock_stdout:
            patterns.draw_pyramid(3)
            self.assertEqual(mock_stdout.getvalue(), "  *\n ***\n*****\n  ***** \n")

    def test_14_primes(self):
        
        text_capture = StringIO()
        sys.stdout = text_capture
        patterns.draw_triangle_prime(5)

        self.assertEqual("""2 
3 5 
7 11 13 
17 19 23 29 
31 37 41 43 47 
""",text_capture.getvalue())

    def test_15_primes(self):
        
        text_capture = StringIO()
        sys.stdout = text_capture
        patterns.draw_triangle_prime(10)

        self.assertEqual("""2 
3 5 
7 11 13 
17 19 23 29 
31 37 41 43 47 
53 59 61 67 71 73 
79 83 89 97 101 103 107 
109 113 127 131 137 139 149 151 
157 163 167 173 179 181 191 193 197 
199 211 223 227 229 233 239 241 251 257 
""",text_capture.getvalue())
        
    def test_tower_of_hanoi_1(self):
        self.assertEqual(patterns.tower_of_hanoi(1, 'A', 'B', 'C'), [('A', 'C')])

    def test_tower_of_hanoi_2(self):
        self.assertEqual(patterns.tower_of_hanoi(2, 'A', 'B', 'C'), [('A', 'B'), ('A', 'C'), ('B', 'C')])

    def test_tower_of_hanoi_3(self):
        self.assertEqual(patterns.tower_of_hanoi(3, 'A', 'B', 'C'), [('A', 'C'), ('A', 'B'), ('C', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('A', 'C')])

    def test_tower_of_hanoi_4(self):
        self.assertEqual(patterns.tower_of_hanoi(4, 'A', 'B', 'C'), [
            ('A', 'C'), ('A', 'B'), ('C', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('A', 'C'),
            ('A', 'B'), ('C', 'B'), ('C', 'A'), ('B', 'A'), ('C', 'B'), ('A', 'C'), ('A', 'B'),
            ('C', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('A', 'C'), ('A', 'B'), ('C', 'B'),
            ('A', 'C'), ('B', 'A'), ('B', 'C'), ('A', 'C')
        ])

    def test_tower_of_hanoi_5(self):
        self.assertEqual(patterns.tower_of_hanoi(5, 'A', 'B', 'C'), [
            ('A', 'C'), ('A', 'B'), ('C', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('A', 'C'),
            ('A', 'B'), ('C', 'B'), ('C', 'A'), ('B', 'A'), ('C', 'B'), ('A', 'C'), ('A', 'B'),
            ('C', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('A', 'C'), ('A', 'B'), ('C', 'B'),
            ('A', 'C'), ('B', 'A'), ('B', 'C'), ('A', 'C'),
            ('A', 'B'), ('C', 'B'), ('C', 'A'), ('B', 'A'), ('C', 'B'), ('A', 'C'), ('A', 'B'),
            ('C', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('A', 'C'), ('A', 'B'), ('C', 'B'),
            ('A', 'C'), ('B', 'A'), ('B', 'C'), ('A', 'C'), ('A', 'B'), ('C', 'B'), ('A', 'C'),
            ('B', 'A'), ('B', 'C'), ('A', 'C')
        ])

        
    
if __name__ == '__main__':
    unittest.main()