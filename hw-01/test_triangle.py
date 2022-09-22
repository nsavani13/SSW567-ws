import unittest

from triangle import TypesOfTriangles


class TestTriangle(unittest.TestCase):
    def test_init(self): # test initial values
        result = TypesOfTriangles(3, 4, 5)
        self.assertEqual(result.a, 3)
        self.assertEqual(result.b, 4)
        self.assertEqual(result.c, 5)

    def test_valid_triangle(self):
        r = TypesOfTriangles(10,3,2)
        self.assertGreater(r.a + r.b, r.c)
        self.assertGreater(r.b + r.c, r.a)
        self.assertGreater(r.c + r.a, r.b)

    def test_equi(self): # test if trianlge is equilateral
        result = TypesOfTriangles(3, 3, 3)
        self.assertEqual(result.classify_triangle(), 'equilateral', msg='equilateral triangle')

    def test_isosceles(self):# test if triangle is isosceles
        result = TypesOfTriangles(3, 4, 3)
        self.assertEqual(result.classify_triangle(), 'isosceles', msg='isosceles triangle')

    def test_scel(self):# test if triangle is scalene
        result = TypesOfTriangles(2, 3, 5)
        self.assertEqual(result.classify_triangle(), 'scalene', msg='scalene triangle')

    def test_scalene_right(self):# test if trianlge is scalene and right
        result = TypesOfTriangles(4, 3, 5)
        self.assertEqual(result.classify_triangle(), 'scalene and right', msg='scalene and right triangle')

    def test_isosceles_right(self):# test if trianlge is isosceles and right
        result = TypesOfTriangles(7, 7, 9.89)
        self.assertEqual(result.classify_triangle(), 'isosceles and right', msg='7,7,9.89 is isosceles and right triangle')


    def test_not_equi(self):# test if it is not equilateral
        result = TypesOfTriangles(2, 3, 3)
        self.assertFalse(result.equilateral())

    def test_not_isosceles(self):# test if it is not triangle is isosceles
        result = TypesOfTriangles(3, 3, 3)
        self.assertFalse(result.isosceles())

    def test_not_scel(self):# test if it is not triangle is scalene
        result = TypesOfTriangles(3, 3, 5)
        self.assertFalse(result.scalene())

    def test_not_right(self):# test if triangle is not right
        result = TypesOfTriangles(4, 6, 5)
        self.assertFalse(result.right())





if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
