import unittest


def solution(nums, target):
    """
    1. sort and find the target index
    2. check if target is inside or outside the list
    3. if outside, loop from max value backward
    4. if inside, find the closest to target and then loop backward
    2. find the closest item to target
    3. find the expected item in the left section that add up to the target
    """
    pass


class SolutionTestCase(unittest.TestCase):
    """
    """

    def test_solution_case_one(self):
        nums = [2, 7, 11, 15]
        self.assertEqual([0, 1], solution(nums, 9))

    def test_solution_case_two(self):
        nums = [3, 2, 4]
        self.assertEqual([1, 2], solution(nums, 6))

    def test_solution_case_three(self):
        nums = [3, 3]
        self.assertEqual([0, 1], solution(nums, 6))


if __name__ == '__main__':
    unittest.main()
