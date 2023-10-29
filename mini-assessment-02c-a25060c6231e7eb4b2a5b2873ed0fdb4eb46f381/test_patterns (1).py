import unittest
from io import StringIO
import sys
from unittest.mock import patch
import patterns

class MyTestCase(unittest.TestCase):

    @patch("sys.stdin", StringIO("Square\n"))
    def test_1_shape(self):

        text_capture = StringIO()
        sys.stdout = text_capture
        self.assertEqual(patterns.get_shape(),'square')
    
    @patch("sys.stdin", StringIO("pYraMid\n"))
    def test_2_shape(self):

        text_capture = StringIO()
        sys.stdout = text_capture
        self.assertEqual(patterns.get_shape(),'pyramid')

    @patch("sys.stdin", StringIO("5\n"))
    def test_3_height(self):

        text_capture = StringIO()
        sys.stdout = text_capture
        self.assertIsInstance(patterns.get_height(),int)

    def test_4_square(self):
        
        text_capture = StringIO()
        sys.stdout = text_capture
        patterns.draw_square(4)

        self.assertEqual("""****
****
****
****
""",text_capture.getvalue())

    def test_5_square(self):
        
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
        
        text_capture = StringIO()
        sys.stdout = text_capture
        patterns.draw_triangle_reversed(3)

        self.assertEqual("""1 1 1 
2 2 
3 
""",text_capture.getvalue())

    def test_7_triangle(self):
        
        text_capture = StringIO()
        sys.stdout = text_capture
        patterns.draw_triangle_reversed(5)

        self.assertEqual("""1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5 
""",text_capture.getvalue())

    def test_8_triangle(self):
        
        text_capture = StringIO()
        sys.stdout = text_capture
        patterns.draw_triangle(3)

        self.assertEqual("""1 
1 2 
1 2 3 
""",text_capture.getvalue())

    def test_9_triangle(self):
        
        text_capture = StringIO()
        sys.stdout = text_capture
        patterns.draw_triangle(5)

        self.assertEqual("""1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
""",text_capture.getvalue())

    def test_10_triangle_multiplication(self):
        
        text_capture = StringIO()
        sys.stdout = text_capture
        patterns.draw_triangle_multiplication(6)

        self.assertEqual("""1 
2 4 
3 6 9 
4 8 12 16 
5 10 15 20 25 
6 12 18 24 30 36 
""",text_capture.getvalue())

    def test_11_triangle_multiplication(self):
        
        text_capture = StringIO()
        sys.stdout = text_capture
        patterns.draw_triangle_multiplication(10)

        self.assertEqual("""1 
2 4 
3 6 9 
4 8 12 16 
5 10 15 20 25 
6 12 18 24 30 36 
7 14 21 28 35 42 49 
8 16 24 32 40 48 56 64 
9 18 27 36 45 54 63 72 81 
10 20 30 40 50 60 70 80 90 100 
""",text_capture.getvalue())


    def test_12_pyramid(self):
        
        text_capture = StringIO()
        sys.stdout = text_capture
        patterns.draw_pyramid(3)

        self.assertEqual("""  *
 ***
*****
""",text_capture.getvalue())

    def test_13_pyramid(self):
        
        text_capture = StringIO()
        sys.stdout = text_capture
        patterns.draw_pyramid(5)

        self.assertEqual("""    *
   ***
  *****
 *******
*********
""",text_capture.getvalue())

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