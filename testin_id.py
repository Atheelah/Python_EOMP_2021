import unittest
import random


def ran_nums():
    nums = random.sample(range(1, 49), 6)
    print(nums)
    return nums


class RandomNums(unittest.TestCase):
    def setUp(self):
        self.a = 1
        self.b = 49

    def test_gen_age(self):
        ran_nums()
        self.assertTrue(self.a >= 1 and self.b <= 49);


if __name__ == '__main__':
    unittest.main()
