import unittest

from src.main.v8n import v8n


class TestV8N(unittest.TestCase):
    def test_greater_than(self):
        validator = v8n().greater_than(2)

        self.assertTrue(validator.test(3))
        self.assertFalse(validator.test(2))
        self.assertFalse(validator.test(1))

    def test_greater_or_equal_than(self):
        validator = v8n().greater_or_equal_than(2)

        self.assertTrue(validator.test(3))
        self.assertTrue(validator.test(2))
        self.assertFalse(validator.test(1))

    def test_less_than(self):
        validator = v8n().less_than(2)

        self.assertFalse(validator.test(3))
        self.assertFalse(validator.test(2))
        self.assertTrue(validator.test(1))

    def test_less_or_equal_than(self):
        validator = v8n().less_or_equal_than(2)

        self.assertFalse(validator.test(3))
        self.assertTrue(validator.test(2))
        self.assertTrue(validator.test(1))


if __name__ == '__main__':
    unittest.main()
