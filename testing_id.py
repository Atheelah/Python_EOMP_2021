import unittest
import rsaidnumber


def check():
    identity = rsaidnumber.parse("0007170122084")

    return identity


class ValidID(unittest.TestCase):
    def setUp(self):
        a = rsaidnumber.parse("0007170122084")

    def TestValid(self):
        check()
        self.assertEqual(check())

    def TestId(self):
        self.assertTrue(rsaidnumber.RSA_ID_LENGTH, 13)


if __name__ == '__main__':
    unittest.main()
