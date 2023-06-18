import compute_stats
import unittest


class LestLenFuncTest(unittest.TestCase):

    def test_good_example(self):
        result = compute_stats.get_list_len([1, 2])
        self.assertEqual(result, 2)

    def test_any_types_working_well(self):
        result = compute_stats.get_list_len([1, 2, 'asd'])
        self.assertEqual(result, 3)


class IntSumTestFunc(unittest.TestCase):

    def test_get_numbers_total_sum(self):
        result = compute_stats.int_sum([1,2])
        self.assertEqual(result, 3)

    def test_wrong_value_logic(self):
        self.assertRaises(TypeError, compute_stats.int_sum, [1, 'asd'])
