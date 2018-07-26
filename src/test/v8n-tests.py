import unittest
from array import array

from src.py_v8n import v8n


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

    def test_equal(self):
        validator = v8n().equal(2)
        self.assertTrue(validator.test(2))
        self.assertFalse(validator.test(3))

    def test_length(self):
        validator = v8n().length(2)
        self.assertTrue(validator.test("12"))
        self.assertTrue(validator.test([1, 2]))
        self.assertFalse(validator.test("1"))
        self.assertFalse(validator.test([1]))

    def test_min_length(self):
        validator = v8n().min_length(2)
        self.assertTrue(validator.test("12"))
        self.assertTrue(validator.test("123"))
        self.assertFalse(validator.test("1"))
        self.assertTrue(validator.test([1, 2]))
        self.assertTrue(validator.test([1, 2, 3]))
        self.assertFalse(validator.test([1]))

    def test_max_length(self):
        validator = v8n().max_length(3)
        self.assertTrue(validator.test([1, 2]))
        self.assertTrue(validator.test("12"))
        self.assertTrue(validator.test([1, 2, 3]))
        self.assertTrue(validator.test("123"))
        self.assertFalse(validator.test([1, 2, 3, 4]))
        self.assertFalse(validator.test("1234"))

    def test_divisible_by(self):
        validator = v8n().divisible_by(5)
        self.assertTrue(validator.test(10))
        self.assertFalse(validator.test(11))

    def test_odd(self):
        validator = v8n().odd()
        self.assertTrue(validator.test(3))
        self.assertFalse(validator.test(4))

    def test_even(self):
        validator = v8n().even()
        self.assertFalse(validator.test(3))
        self.assertTrue(validator.test(4))

    def test_between(self):
        validator = v8n().between(2, 4)
        self.assertTrue(validator.test(2))
        self.assertTrue(validator.test(3))
        self.assertTrue(validator.test(4))
        self.assertFalse(validator.test(1))
        self.assertFalse(validator.test(5))

    def test_str_(self):
        validator = v8n().str_()
        self.assertTrue(validator.test("string"))
        self.assertFalse(validator.test(1))

    def test_int_(self):
        validator = v8n().int_()
        self.assertTrue(validator.test(1))
        self.assertFalse(validator.test("string"))

    def test_bool_(self):
        validator = v8n().bool_()
        self.assertTrue(validator.test(True))
        self.assertFalse(validator.test("string"))

    def test_empty(self):
        validator = v8n().empty()
        self.assertTrue(validator.test([]))
        self.assertTrue(validator.test(""))
        self.assertFalse(validator.test([1]))
        self.assertFalse(validator.test("a"))

    def test_first(self):
        validator_str = v8n().first("a")
        self.assertTrue(validator_str.test("a string"))
        self.assertFalse(validator_str.test("b string"))
        validator_list = v8n().first(1)
        self.assertTrue(validator_list.test([1, 2, 3]))
        self.assertFalse(validator_list.test([4, 5, 6]))

    def test_last(self):
        validator_str = v8n().last("a")
        self.assertTrue(validator_str.test("string a"))
        self.assertFalse(validator_str.test("string b"))
        validator_list = v8n().last(3)
        self.assertTrue(validator_list.test([1, 2, 3]))
        self.assertFalse(validator_list.test([4, 5, 6]))

    def test_negative(self):
        validator = v8n().negative()
        self.assertTrue(validator.test(-1))
        self.assertFalse(validator.test(1))

    def test_positive(self):
        validator = v8n().positive()
        self.assertFalse(validator.test(-1))
        self.assertTrue(validator.test(1))

    def test_includes(self):
        validator_str = v8n().includes("a")
        self.assertTrue(validator_str.test("a string"))
        self.assertFalse(validator_str.test("b string"))
        validator_list = v8n().includes(1)
        self.assertTrue(validator_list.test([1, 2, 3]))
        self.assertFalse(validator_list.test([4, 5, 6]))

    def test_none(self):
        validator = v8n().none()
        self.assertTrue(validator.test(None))
        self.assertFalse(validator.test("string"))
        self.assertFalse(validator.test(1))

    def test_list_(self):
        validator = v8n().list_()
        self.assertTrue(validator.test([1]))
        self.assertFalse(validator.test(1))

    def test_not_greater_than(self):
        validator = v8n().not_().greater_than(2)
        self.assertFalse(validator.test(3))
        self.assertTrue(validator.test(2))
        self.assertTrue(validator.test(1))

    def test_not_greater_or_equal_than(self):
        validator = v8n().not_().greater_or_equal_than(2)
        self.assertFalse(validator.test(3))
        self.assertFalse(validator.test(2))
        self.assertTrue(validator.test(1))

    def test_not_less_than(self):
        validator = v8n().not_().less_than(2)
        self.assertTrue(validator.test(3))
        self.assertTrue(validator.test(2))
        self.assertFalse(validator.test(1))

    def test_not_less_or_equal_than(self):
        validator = v8n().not_().less_or_equal_than(2)
        self.assertTrue(validator.test(3))
        self.assertFalse(validator.test(2))
        self.assertFalse(validator.test(1))

    def test_not_equal(self):
        validator = v8n().not_().equal(2)
        self.assertFalse(validator.test(2))
        self.assertTrue(validator.test(3))

    def test_not_length(self):
        validator = v8n().not_().length(2)
        self.assertFalse(validator.test("12"))
        self.assertFalse(validator.test([1, 2]))
        self.assertTrue(validator.test("1"))
        self.assertTrue(validator.test([1]))

    def test_not_min_length(self):
        validator = v8n().not_().min_length(2)
        self.assertFalse(validator.test("12"))
        self.assertFalse(validator.test("123"))
        self.assertTrue(validator.test("1"))
        self.assertFalse(validator.test([1, 2]))
        self.assertFalse(validator.test([1, 2, 3]))
        self.assertTrue(validator.test([1]))

    def test_not_max_length(self):
        validator = v8n().not_().max_length(3)
        self.assertFalse(validator.test([1, 2]))
        self.assertFalse(validator.test("12"))
        self.assertFalse(validator.test([1, 2, 3]))
        self.assertFalse(validator.test("123"))
        self.assertTrue(validator.test([1, 2, 3, 4]))
        self.assertTrue(validator.test("1234"))

    def test_not_divisible_by(self):
        validator = v8n().not_().divisible_by(5)
        self.assertFalse(validator.test(10))
        self.assertTrue(validator.test(11))

    def test_not_odd(self):
        validator = v8n().not_().odd()
        self.assertFalse(validator.test(3))
        self.assertTrue(validator.test(4))

    def test_not_even(self):
        validator = v8n().not_().even()
        self.assertTrue(validator.test(3))
        self.assertFalse(validator.test(4))

    def test_not_between(self):
        validator = v8n().not_().between(2, 4)
        self.assertFalse(validator.test(2))
        self.assertFalse(validator.test(3))
        self.assertFalse(validator.test(4))
        self.assertTrue(validator.test(1))
        self.assertTrue(validator.test(5))

    def test_not_str_(self):
        validator = v8n().not_().str_()
        self.assertFalse(validator.test("string"))
        self.assertTrue(validator.test(1))

    def test_not_int_(self):
        validator = v8n().not_().int_()
        self.assertFalse(validator.test(1))
        self.assertTrue(validator.test("string"))

    def test_not_bool_(self):
        validator = v8n().not_().bool_()
        self.assertFalse(validator.test(True))
        self.assertTrue(validator.test("string"))

    def test_not_empty(self):
        validator = v8n().not_().empty()
        self.assertFalse(validator.test([]))
        self.assertFalse(validator.test(""))
        self.assertTrue(validator.test([1]))
        self.assertTrue(validator.test("a"))

    def test_not_first(self):
        validator_str = v8n().not_().first("a")
        self.assertFalse(validator_str.test("a string"))
        self.assertTrue(validator_str.test("b string"))
        validator_list = v8n().not_().first(1)
        self.assertFalse(validator_list.test([1, 2, 3]))
        self.assertTrue(validator_list.test([4, 5, 6]))

    def test_not_last(self):
        validator_str = v8n().not_().last("a")
        self.assertFalse(validator_str.test("string a"))
        self.assertTrue(validator_str.test("string b"))
        validator_list = v8n().not_().last(3)
        self.assertFalse(validator_list.test([1, 2, 3]))
        self.assertTrue(validator_list.test([4, 5, 6]))

    def test_not_negative(self):
        validator = v8n().not_().negative()
        self.assertFalse(validator.test(-1))
        self.assertTrue(validator.test(1))

    def test_not_positive(self):
        validator = v8n().not_().positive()
        self.assertTrue(validator.test(-1))
        self.assertFalse(validator.test(1))

    def test_not_includes(self):
        validator_str = v8n().not_().includes("a")
        self.assertFalse(validator_str.test("a string"))
        self.assertTrue(validator_str.test("b string"))
        validator_list = v8n().not_().includes(1)
        self.assertFalse(validator_list.test([1, 2, 3]))
        self.assertTrue(validator_list.test([4, 5, 6]))

    def test_not_none(self):
        validator = v8n().not_().none()
        self.assertFalse(validator.test(None))
        self.assertTrue(validator.test("string"))
        self.assertTrue(validator.test(1))

    def test_not_list_(self):
        validator = v8n().not_().list_()
        self.assertFalse(validator.test([1]))
        self.assertTrue(validator.test(1))

    def test_float_(self):
        validator = v8n().float_()
        self.assertFalse(validator.test(1))
        self.assertTrue(validator.test(1.0))

    def test_dict_(self):
        validator = v8n().dict_()
        self.assertFalse(validator.test(1))
        self.assertTrue(validator.test({'a': 1}))

    def test_set_(self):
        validator = v8n().set_()
        self.assertFalse(validator.test(1))
        self.assertTrue(validator.test({1, 2, 3}))

    def test_tuple_(self):
        validator = v8n().tuple_()
        self.assertFalse(validator.test(1))
        self.assertTrue(validator.test((1, 2)))

    def test_of_type(self):
        validator = v8n().of_type(array)
        self.assertFalse(validator.test(1))
        arr = array('i')
        arr.append(-1)
        arr.append(1)
        self.assertTrue(validator.test(arr))

    def test_every(self):
        validator = v8n().list_().every().int_().between(1, 10)
        self.assertFalse(validator.test([1, 5, 11]))
        self.assertFalse(validator.test([1, 5, '9']))
        self.assertTrue(validator.test([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

    def test_validate(self):
        validator = v8n().float_().between(0, 1)
        with self.assertRaises(ValueError, msg="my_var must:\n\t- be between 0 and 1 (inclusive)"):
            validator.validate(2.0, value_name="my_var")


if __name__ == '__main__':
    unittest.main()
