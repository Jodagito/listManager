from list_manager import (subtract_elements, multiply_elements,
                          divide_elements,
                          remove_repeated_elements, return_element_index,
                          return_common_elements, return_uncommon_elements,
                          element_average, array_average, array_mode,
                          odd_array_median, pair_array_median)
import unittest

sample_array = [14, 44, 80, 3, 40, 44, 10, 80, 25, 17, 34]
sample_array1 = [20, 3, 25, 6, 18, 32, 44, 10]
sample_array2 = [-23, 23.0, 34, 4.5, 0, 0, -1, -13, 3.5]
sample_array3 = [23, -23, 34, 4.5]


class TestListManager(unittest.TestCase):
    def test_subtract_elements(self):
        self.assertEqual([-30, -36, 77, -37, -4, 34, -70, 55, 8, -17],
                         subtract_elements(sample_array))
        self.assertEqual([-46.0, -11.0, 29.5, 4.5, 0, 1, 12, -16.5],
                         subtract_elements(sample_array2))

    def test_multiply_elements(self):
        self.assertEqual(multiply_elements(sample_array), [616, 3520, 240, 120,
                                                           1760, 440, 800,
                                                           2000, 425, 578])
        self.assertEqual(multiply_elements(sample_array2), [-529, 782, 153, 0,
                                                            0, 0, 13,
                                                            -45.5])

    def test_divide_elements(self):
        self.assertEqual(divide_elements(sample_array), [0.3181818181818182,
                                                         0.55,
                                                         26.666666666666668,
                                                         0.075,
                                                         0.9090909090909091,
                                                         4.4, 0.125, 3.2,
                                                         1.4705882352941178,
                                                         0.5])
        self.assertEqual(divide_elements(sample_array2), [-1.0,
                                                          0.6764705882352942,
                                                          7.555555555555555,
                                                          -4.5,
                                                          0.07692307692307693,
                                                          -3.7142857142857144])

    def test_return_common_elements(self):
        [self.assertIn(x, sample_array1) for x in return_common_elements(
            sample_array, sample_array1)]
        [self.assertIn(x, sample_array3) for x in return_common_elements(
            sample_array2, sample_array3)]

    def test_return_uncommon_elements(self):
        [self.assertNotIn(x, sample_array1) for x in return_uncommon_elements(
            sample_array, sample_array1)]
        [self.assertNotIn(x, sample_array3) for x in return_uncommon_elements(
            sample_array2, sample_array3)]

    def test_return_element_index(self):
        self.assertEqual(return_element_index(sample_array, 44), [1, 5])
        self.assertEqual(return_element_index(sample_array2, 0), [4, 5])

    def test_element_average(self):
        self.assertEqual(element_average(sample_array, 80), 18.181818181818183)
        self.assertEqual(element_average(sample_array2, 0), 22.22222222222222)

    def test_array_average(self):
        self.assertEqual(array_average(sample_array), 35.54545454545455)
        self.assertEqual(array_average(sample_array2), 3.111111111111111)

    def test_array_mode(self):
        self.assertEqual(array_mode(sample_array), 2)
        self.assertEqual(array_mode(sample_array2), 2)

    def test_odd_array_median(self):
        self.assertEqual(odd_array_median(sample_array), 44)
        self.assertEqual(odd_array_median(sample_array2), 0)

    def test_pair_array_median(self):
        self.assertEqual(pair_array_median(sample_array1), 12.0)
        self.assertEqual(pair_array_median(sample_array3), 5.5)

    def test_remove_repeated_elements(self):
        self.assertEqual(remove_repeated_elements(sample_array), [14, 3, 40,
                                                                  10, 25, 17,
                                                                  34])
        self.assertEqual(remove_repeated_elements(sample_array2), [-23, 23.0,
                                                                   34, 4.5,
                                                                   -1, -13,
                                                                   3.5])


if __name__ == '__main__':
    unittest.main()

print("All tests were correctly finished.")
