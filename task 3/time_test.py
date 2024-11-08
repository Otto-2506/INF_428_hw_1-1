import math
import unittest

def calculate_time_difference(hour1, hour2):
   
    forward_diff = abs(hour2 - hour1)
    backward_diff = 24 - forward_diff
    return min(forward_diff, backward_diff)

def time_to_cyclic_features(hour):

    radians = 2 * math.pi * (hour % 24) / 24
    sin_time = math.sin(radians)
    cos_time = math.cos(radians)
    return sin_time, cos_time

def time_difference(hour1, hour2):
    return min(abs(hour2 - hour1), 24 - abs(hour2 - hour1))

class TestCyclicTime(unittest.TestCase):

    # Test 1: Testing for a direct difference without crossing midnight
    def test_direct_difference(self):
        self.assertEqual(calculate_time_difference(1, 3), 2)
        self.assertEqual(calculate_time_difference(5, 8), 3)

    # Test 2: Testing difference crossing midnight
    def test_midnight_crossing_difference(self):
        self.assertEqual(calculate_time_difference(23, 1), 2)
        self.assertEqual(calculate_time_difference(22, 2), 4)

    # Test 3: Testing difference for the same hour
    def test_same_time_difference(self):
        self.assertEqual(calculate_time_difference(12, 12), 0)

    # Test 4: Testing opposite points on the clock
    def test_opposite_hours(self):
        self.assertEqual(calculate_time_difference(0, 12), 12)
        self.assertEqual(calculate_time_difference(6, 18), 12)

    # Test 5: Testing boundary cases like 0 and 24
    def test_boundary_cases(self):
        self.assertEqual(calculate_time_difference(0, 23), 1)
        self.assertEqual(calculate_time_difference(0, 24), 0)

    # Test 6: Testing time_to_cyclic_features for known values
    def test_time_to_cyclic_features(self):
        sin0, cos0 = time_to_cyclic_features(0)
        sin6, cos6 = time_to_cyclic_features(6)
        sin12, cos12 = time_to_cyclic_features(12)
        sin18, cos18 = time_to_cyclic_features(18)
        
        self.assertAlmostEqual(sin0, 0, delta=0.01)
        self.assertAlmostEqual(cos0, 1, delta=0.01)
        self.assertAlmostEqual(sin6, 1, delta=0.01)
        self.assertAlmostEqual(cos6, 0, delta=0.01)
        self.assertAlmostEqual(sin12, 0, delta=0.01)
        self.assertAlmostEqual(cos12, -1, delta=0.01)
        self.assertAlmostEqual(sin18, -1, delta=0.01)
        self.assertAlmostEqual(cos18, 0, delta=0.01)

    # Test 7: Testing time_difference for known cyclic differences
    def test_time_difference(self):
        self.assertAlmostEqual(time_difference(23, 1), 2, delta=0.1)
        self.assertAlmostEqual(time_difference(1, 23), 2, delta=0.1)
        self.assertAlmostEqual(time_difference(0, 12), 12, delta=0.1)
        self.assertAlmostEqual(time_difference(6, 18), 12, delta=0.1)

if __name__ == "__main__":
    unittest.main()
