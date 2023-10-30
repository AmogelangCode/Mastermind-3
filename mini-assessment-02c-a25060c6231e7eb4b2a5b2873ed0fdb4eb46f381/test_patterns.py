import unittest
from io import StringIO
import sys
from unittest.mock import patch
import patterns

class MyTestCase(unittest.TestCase):

    def test_1_shape(self):
        

    

    def test_2_shape(self):
        pass


    def test_3_height(self):
        pass

    def test_4_square(self):
        pass

    def test_5_square(self):
        
        pass

    def test_6_triangle(self):
        
        pass

    def test_7_triangle(self):
        
        pass

    def test_8_triangle(self):
        
        pass
    def test_9_triangle(self):
        
        pass

    def test_10_triangle_multiplication(self):
        
        pass

    def test_11_triangle_multiplication(self):
        
        pass


    def test_12_pyramid(self):
        
        pass

    def test_13_pyramid(self):
        
        pass

    def test_14_primes(self):
        
        pass

    def test_15_primes(self):
        
        pass
        
class TestTowerOfHanoi(unittest.TestCase):

    def assert_valid_hanoi_moves(self, n, source, auxiliary, target, moves):
        # Check that the number of moves is correct for n disks
        expected_moves = 2 ** n - 1
        self.assertEqual(len(moves), expected_moves)

        # Check that the moves are valid
        for move in moves:
            self.assertIn(move[0], [source, auxiliary, target])
            self.assertIn(move[1], [source, auxiliary, target])
            self.assertNotEqual(move[0], move[1])

    def test_tower_of_hanoi_1(self):
        n = 1
        source, auxiliary, target = 'A', 'B', 'C'
        moves = tower_of_hanoi(n, source, auxiliary, target)
        self.assert_valid_hanoi_moves(n, source, auxiliary, target, moves)


    def test_tower_of_hanoi_2(self):
        n = 2
        source, auxiliary, target = 'A', 'B', 'C'
        moves = tower_of_hanoi(n, source, auxiliary, target)
        self.assert_valid_hanoi_moves(n, source, auxiliary, target, moves)


    def test_tower_of_hanoi_3(self):
        n = 3
        source, auxiliary, target = 'A', 'B', 'C'
        moves = tower_of_hanoi(n, source, auxiliary, target)
        self.assert_valid_hanoi_moves(n, source, auxiliary, target, moves)

    def test_tower_of_hanoi_4(self):
        n = 4
        source, auxiliary, target = 'A', 'B', 'C'
        moves = tower_of_hanoi(n, source, auxiliary, target)
        self.assert_valid_hanoi_moves(n, source, auxiliary, target, moves)

    def test_tower_of_hanoi_5(self):
        n = 5
        source, auxiliary, target = 'X', 'Y', 'Z'
        moves = tower_of_hanoi(n, source, auxiliary, target)
        self.assert_valid_hanoi_moves(n, source, auxiliary, target, moves)


        
    
if __name__ == '__main__':
    unittest.main()