from calculator import *
import unittest
c= Calculator()
class TestCalculator(unittest.TestCase):
   
    def test_add(self):
        return self.assertEqual(c.add(9,1), 7,"Incorrect")
        
    def test_subtract(self):
        return self.assertEqual(c.add(9,1), 7,"Incorrect")
    
    def test_division(self):
        return self.assertEqual(c.divide(1, 0),'Can not divide by zero.', "incorrect")
    
    def nth_root(self):
        return self.assertEqual(c.root(-4) , 'Invalid input',"Incorrect")
        
    def test_invalid_value(self):
        assert c.add('a', 'b') == 'Invalid input'
        
        assert c.subtract('a', 'b') == 'Invalid input'
        
        assert c.multiply('a', 'b') == 'Invalid input'
        
        assert c.divide('a', 'b') == 'Invalid input'
        
        assert c.root('a') == 'Invalid input'
        
    
    
    def test_memory(self):
        c.reset_memory()

        assert c.add(0) == 0
        assert c.add(1) == 1
        assert c.add(1) == 2

        c.reset_memory()

        assert c.subtract(0) == 0
        assert c.subtract(1) == -1
        assert c.subtract(1) == -2

        c.reset_memory()

        assert c.multiply(1, 1) == 1
        assert c.multiply(2) == 2
        assert c.multiply(2) == 4

        c.reset_memory()

        assert c.divide(2, 20) == 10
        assert c.divide(2) == 5
        assert c.divide(5) == 1

        c.reset_memory()

        assert c.root(2) == 4
        assert c.root() == 16
        assert c.root() == 256

        