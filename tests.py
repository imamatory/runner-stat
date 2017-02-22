import unittest
from main import min_time_for


class TestTaskRunner(unittest.TestCase):

    def test_unreachable_distance(self):
        """
        Should raise exception when sum of passed distance
        less then required distance
        """
        data = (1, 1, 1)
        with self.assertRaises(ValueError):
            min_time_for(4, data)

    def test_should_work_1(self):
        data = (20, 30, 5, 60, 4)
        self.assertEqual(min_time_for(70, data), 3)

    def test_should_work_2(self):
        data = (2, 3, 5, 6, 4)
        self.assertEqual(min_time_for(16, data), 4)

    def test_one_from_left(self):
        data = (20, 3, 5, 6, 7)
        self.assertEqual(min_time_for(15, data), 1)

    def test_one_from_right(self):
        data = (7, 3, 5, 6, 20)
        self.assertEqual(min_time_for(15, data), 1)
