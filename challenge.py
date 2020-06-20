import math

def square_area(side):
    """Returns the area of a square"""
    # You have to code here
    # REMEMBER: Tests first!!!
    return side ** 2


def rectangle_area(base, height):
    """Returns the area of a rectangle"""
    # You have to code here
    # REMEMBER: Tests first!!!
    return base * height


def triangle_area(base, height):
    """Returns the area of a triangle"""
    # You have to code here
    # REMEMBER: Tests first!!!
    return (base * height) / 2


def rhombus_area(diagonal_1, diagonal_2):
    """Returns the area of a rhombus"""
    # You have to code here
    # REMEMBER: Tests first!!!
    return (diagonal_1 * diagonal_2) / 2


def trapezoid_area(base_minor, base_major, height):
    """Returns the area of a trapezoid"""
    # You have to code here
    # REMEMBER: Tests first!!!
    return height * ((base_minor + base_major) / 2)


def regular_polygon_area(perimeter, apothem):
    """Returns the area of a regular polygon"""
    # You have to code here
    # REMEMBER: Tests first!!!
    return (apothem ** 2) * perimeter * math.tan(180 / perimeter)


def circumference_area(radius):
    """Returns the area of a circumference"""
    # You have to code here
    # REMEMBER: Tests first!!!
    # Use math.pi for π value
    return math.pi * (radius ** 2)


if __name__ == '__main__':
    import unittest

    class GeometrySuite(unittest.TestCase):

        def setUp(self):
            # Initialize the needed values for the tests
            self.square = {
                1:  1,
                4: 2,
                16: 4,
                225: 15
            }

            self.rectangle = {
                2:  [1, 2],
                12: [3, 4],
                35: [5, 7],
                48: [6, 8]
            }

            self.triangle = {
                1:  [1, 2],
                6: [3, 4],
                20: [5, 8],
                24: [6, 8]
            }

            self.rhombus = {
                1:  [1, 2],
                6: [3, 4],
                20: [5, 8],
                24: [6, 8]
            }

            self.trapezoid = {
                4.5:  [1, 2, 3],
                17.5: [3, 4, 5],
                39.0: [5, 8, 6],
                42.0: [6, 8, 6]
            }

            self.regular_polygon = {
                5.354760841404618:  [1, 2],
                15.361938690219024: [3, 4],
                2480.150689823727: [5, 8],
                -2459.6471795121697: [6, 8]
            }

            self.circle = {
                3.141592653589793:  1
            }

        def test_square_area(self):
            # Make this test first...
            for key, value in self.square.items():
                self.assertEqual(key, square_area(value))

        def test_rectangle_area(self):
            # Make this test first...
            for key, value in self.rectangle.items():
                self.assertEqual(key, rectangle_area(value[0], value[1]))

        def test_triangle_area(self):
            # Make this test first...
            for key, value in self.triangle.items():
                self.assertEqual(key, triangle_area(value[0], value[1]))

        def test_rhombus_area(self):
            # Make this test first...
            for key, value in self.rhombus.items():
                self.assertEqual(key, rhombus_area(value[0], value[1]))

        def test_trapezoid_area(self):
            # Make this test first...
            for key, value in self.trapezoid.items():
                # base_minor, base_major, height
                self.assertEqual(key, trapezoid_area(value[0], value[1], value[2]))

        def test_regular_polygon_area(self):
            # Make this test first...
            for key, value in self.regular_polygon.items():
                self.assertEqual(key, regular_polygon_area(value[0], value[1]))

        def test_circumference_area(self):
            # Make this test first...
            for key, value in self.circle.items():
                self.assertEqual(key, circumference_area(value))

        def tearDown(self):
            # Delete the needed values for the tests
            del(self.square, self.rectangle)

    unittest.main()
