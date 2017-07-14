from .context import steely
import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_test(self):
        assert True


if __name__ == '__main__':
    unittest.main()
