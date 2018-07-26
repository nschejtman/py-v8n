from .Rule import Rule
from .rules import *


class Validator:
    def __init__(self, chain: list, invert: bool, every: bool):
        self.chain = chain
        self.invert = invert
        self._every = every

    def test(self, *values):
        for value in values:
            for rule in self.chain:
                if not rule.test(value):
                    return False
        return True

    def not_(self):
        return Validator(self.chain, True, False)
    
    def every(self):
        return Validator(self.chain, False, True)
        

    def greater_than(self, a):
        self.chain.append(Rule("be greater than %s" % a, greater_than, [a], self.invert, self._every))
        return Validator(self.chain, False, self._every)

    def greater_or_equal_than(self, a):
        self.chain.append(Rule("be greater or equal than %s" % a, greater_or_equal_than, [a], self.invert, self._every))
        return Validator(self.chain, False, self._every)

    def between(self, a, b):
        self.chain.append(Rule("be between %s and %s (inclusive)" % (a, b), between, [a, b], self.invert, self._every))
        return Validator(self.chain, False, self._every)

    def str_(self):
        self.chain.append(Rule("be a str", str_, [], self.invert, self._every))
        return Validator(self.chain, False, self._every)

    def int_(self):
        self.chain.append(Rule("be an int", int_, [], self.invert, self._every))
        return Validator(self.chain, False, self._every)

    def even(self):
        self.chain.append(Rule("be even", even, [], self.invert, self._every))
        return Validator(self.chain, False, self._every)

    def odd(self):
        self.chain.append(Rule("be odd", odd, [], self.invert, self._every))
        return Validator(self.chain, False, self._every)

    def equal(self, a):
        self.chain.append(Rule("be equal to %s" % a, equal, [a], self.invert, self._every))
        return Validator(self.chain, False, self._every)

    def min_length(self, a):
        self.chain.append(Rule("be of min length %s" % a, min_length, [a], self.invert, self._every))
        return Validator(self.chain, False, self._every)

    def max_length(self, a):
        self.chain.append(Rule("be of max length %s" % a, max_length, [a], self.invert, self._every))
        return Validator(self.chain, False, self._every)

    def length(self, a):
        self.chain.append(Rule("be of length %s" % a, length, [a], self.invert, self._every))
        return Validator(self.chain, False, self._every)

    def none(self):
        self.chain.append(Rule("be none", none, [], self.invert, self._every))
        return Validator(self.chain, False, self._every)

    def first(self, a):
        self.chain.append(Rule("contain first %s" % a, first, [a], self.invert, self._every))
        return Validator(self.chain, False, self._every)

    def last(self, a):
        self.chain.append(Rule("contain last %s" % a, last, [a], self.invert, self._every))
        return Validator(self.chain, False, self._every)

    def list_(self):
        self.chain.append(Rule("be a list", list_, [], self.invert, self._every))
        return Validator(self.chain, False, self._every)

    def bool_(self):
        self.chain.append(Rule("be a bool", bool_, [], self.invert, self._every))
        return Validator(self.chain, False, self._every)

    def less_than(self, a):
        self.chain.append(Rule("be less than %s" % a, less_than, [a], self.invert, self._every))
        return Validator(self.chain, False, self._every)

    def less_or_equal_than(self, a):
        self.chain.append(Rule("be less or equal than %s" % a, less_or_equal_than, [a], self.invert, self._every))
        return Validator(self.chain, False, self._every)

    def includes(self, a):
        self.chain.append(Rule("include %s" % a, includes, [a], self.invert, self._every))
        return Validator(self.chain, False, self._every)

    def positive(self):
        self.chain.append(Rule("be positive", positive, [], self.invert, self._every))
        return Validator(self.chain, False, self._every)

    def negative(self):
        self.chain.append(Rule("be negative", negative, [], self.invert, self._every))
        return Validator(self.chain, False, self._every)

    def empty(self):
        self.chain.append(Rule("be empty", empty, [], self.invert, self._every))
        return Validator(self.chain, False, self._every)

    def divisible_by(self, a):
        self.chain.append(Rule("be divisible by %s" % a, divisible_by, [a], self.invert, self._every))
        return Validator(self.chain, False, self._every)

    def float_(self):
        self.chain.append(Rule("be a float", float_, [], self.invert, self._every))
        return Validator(self.chain, False, self._every)

    def dict_(self):
        self.chain.append(Rule("be a dict", dict_, [], self.invert, self._every))
        return Validator(self.chain, False, self._every)

    def set_(self):
        self.chain.append(Rule("be a set", set_, [], self.invert, self._every))
        return Validator(self.chain, False, self._every)

    def tuple_(self):
        self.chain.append(Rule("be a tuple", tuple_, [], self.invert, self._every))
        return Validator(self.chain, False, self._every)

    def of_type(self, a):
        self.chain.append(Rule("of type %s" % a, of_type, [a], self.invert, self._every))
        return Validator(self.chain, False, self._every)

    def validate(self, value, value_name: str = None):
        error_message = "%s must:\n" % value_name if value_name is not None else "value must:\n"
        should_raise_value_error = False
        for rule in self.chain:
            if not rule.test(value):
                error_message += "\t- %s" % rule.name
                should_raise_value_error = True
        if should_raise_value_error:
            raise ValueError(error_message)
