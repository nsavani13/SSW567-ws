import unittest
from Triangle import classifyTriangle


class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')

    def testEquilateralTrianglesA(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    def testEquilateralTrianglesB(self):
        self.assertEqual(classifyTriangle(5, 5, 5), 'Equilateral', '5,5,5 should be equilateral')

    def testScaleneTrianglesA(self):
        self.assertEqual(classifyTriangle(8, 11, 13), 'Scalene', '8,11,13 should be Scalene')

    def testScaleneTrianglesB(self):
        self.assertEqual(classifyTriangle(15, 34, 32), 'Scalene', '15,34,32 should be Scalene')

    def testIsoscelesTriangles(self):
        self.assertEqual(classifyTriangle(9, 9, 3), 'Isosceles', '9,9,3 should be Isosceles')

    def testIsNotTrianglesA(self):
        self.assertEqual(classifyTriangle(1, 2, 10), 'NotATriangle', '1,2,10 should not be triangle')

    def testIsNotTrianglesB(self):
        self.assertEqual(classifyTriangle(5, 6, 20), 'NotATriangle', '5,6,20 should not be triangle')

    def testInvalidInputTrianglesA(self):
        self.assertEqual(classifyTriangle(-5, -6, 20), 'InvalidInput', '-5,-6,20 should not be triangle')

    def testInvalidInputTrianglesB(self):
        self.assertEqual(classifyTriangle(5, 6, 201), 'InvalidInput', '5,6,201 should not be triangle')

    if __name__ == '__main__':
        print('Running unit tests')
        unittest.main()