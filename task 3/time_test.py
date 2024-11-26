import math
import unittest

def time_to_cyclic_features(time):
    sin_time = math.sin(2 * math.pi * time / 24)
    cos_time = math.cos(2 * math.pi * time / 24)
    return sin_time, cos_time

def time_difference_in_hours(time1, time2):
    sin1, cos1 = time_to_cyclic_features(time1)
    sin2, cos2 = time_to_cyclic_features(time2)
    dot_product = sin1 * sin2 + cos1 * cos2
    angle = math.acos(dot_product)
    diff = (angle / (2 * math.pi)) * 24
    return diff

class TestCyclicTime(unittest.TestCase):

    def test_time_to_cyclic_features(self):
        result = time_to_cyclic_features(23)
        print(f"Test 'test_time_to_cyclic_features': sin={result[0]}, cos={result[1]}")
        self.assertAlmostEqual(result[0], math.sin(2 * math.pi * 23 / 24))
        self.assertAlmostEqual(result[1], math.cos(2 * math.pi * 23 / 24))

    def test_time_difference_in_hours(self):
        diff1 = time_difference_in_hours(23, 1)
        diff2 = time_difference_in_hours(10, 15)
        diff3 = time_difference_in_hours(10, 10)
        diff4 = time_difference_in_hours(0, 12)
        diff5 = time_difference_in_hours(23.5, 0.5)

        print(f"Test 'test_time_difference_in_hours' Case 1 (23, 1): {diff1}")
        print(f"Test 'test_time_difference_in_hours' Case 2 (10, 15): {diff2}")
        print(f"Test 'test_time_difference_in_hours' Case 3 (10, 10): {diff3}")
        print(f"Test 'test_time_difference_in_hours' Case 4 (0, 12): {diff4}")
        print(f"Test 'test_time_difference_in_hours' Case 5 (23.5, 0.5): {diff5}")

        self.assertAlmostEqual(diff1, 2)
        self.assertAlmostEqual(diff2, 5)
        self.assertAlmostEqual(diff3, 0)
        self.assertAlmostEqual(diff4, 12)
        self.assertAlmostEqual(diff5, 1)

if __name__ == "__main__":
    unittest.main()
