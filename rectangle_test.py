import unittest
from rectangle import Rectangle
from points import Point

class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rect1 = Rectangle(0, 0, 4, 4)
        self.rect2 = Rectangle(2, 2, 6, 6)
        self.rect3 = Rectangle(5, 5, 7, 7)

    def test_init(self):
        with self.assertRaises(ValueError):
            Rectangle(2, 2, 1, 1)  # Niepoprawne wymiary

        r = Rectangle(0, 0, 4, 3)
        self.assertEqual(r.pt1, Point(0, 0))
        self.assertEqual(r.pt2, Point(4, 3))

    def test_str_repr(self):
        self.assertEqual(str(self.rect1), "[(0, 0), (4, 4)]")
        self.assertEqual(repr(self.rect1), "Rectangle(0, 0, 4, 4)")

    def test_eq(self):
        rect_copy = Rectangle(0, 0, 4, 4)
        self.assertTrue(self.rect1 == rect_copy)
        self.assertFalse(self.rect1 == self.rect2)

    def test_center(self):
        self.assertEqual(self.rect1.center(), Point(2, 2))

    def test_area(self):
        self.assertEqual(self.rect1.area(), 16)

    def test_move(self):
        moved = self.rect1.move(2, 3)
        self.assertEqual(moved, Rectangle(2, 3, 6, 7))

    def test_intersection(self):
        self.assertEqual(self.rect1.intersection(self.rect2), Rectangle(2, 2, 4, 4))
        with self.assertRaises(ValueError):
            self.rect1.intersection(self.rect3)

    def test_cover(self):
        self.assertEqual(self.rect1.cover(self.rect2), Rectangle(0, 0, 6, 6))

    def test_make4(self):
        r1, r2, r3, r4 = self.rect1.make4()
        self.assertEqual(r1, Rectangle(0, 0, 2, 2))
        self.assertEqual(r2, Rectangle(2, 0, 4, 2))
        self.assertEqual(r3, Rectangle(0, 2, 2, 4))
        self.assertEqual(r4, Rectangle(2, 2, 4, 4))

if __name__ == '__main__':
    unittest.main()
