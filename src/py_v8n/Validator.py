from .Rule import Rule
from .rules import *


class Validator:
    def __init__(self, chain: list, invert: bool):
        self.invert = invert
        self.chain = chain

    def test(self, *values):
        for value in values:
            for rule in self.chain:
                if not rule.test(value):
                    return False
        return True

    def not_(self):
        return Validator(self.chain, True)

    def greater_than(self, a):
        self.chain.append(Rule("be greater than %s" % a, greater_than, [a], self.invert))
        return Validator(self.chain, False)

    def greater_or_equal_than(self, a):
        self.chain.append(Rule("be greater or equal than %s" % a, greater_or_equal_than, [a], self.invert))
        return Validator(self.chain, False)

    def between(self, a, b):
        self.chain.append(Rule("be between %s and %s (inclusive)" % (a, b), between, [a, b], self.invert))
        return Validator(self.chain, False)

    def str_(self):
        self.chain.append(Rule("be a str", str_, [], self.invert))
        return Validator(self.chain, False)

    def int_(self):
        self.chain.append(Rule("be an int", int_, [], self.invert))
        return Validator(self.chain, False)

    def even(self):
        self.chain.append(Rule("be even", even, [], self.invert))
        return Validator(self.chain, False)

    def odd(self):
        self.chain.append(Rule("be odd", odd, [], self.invert))
        return Validator(self.chain, False)

    def equal(self, a):
        self.chain.append(Rule("be equal to %s" % a, equal, [a], self.invert))
        return Validator(self.chain, False)

    def min_length(self, a):
        self.chain.append(Rule("be of min length %s" % a, min_length, [a], self.invert))
        return Validator(self.chain, False)

    def max_length(self, a):
        self.chain.append(Rule("be of max length %s" % a, max_length, [a], self.invert))
        return Validator(self.chain, False)

    def length(self, a):
        self.chain.append(Rule("be of length %s" % a, length, [a], self.invert))
        return Validator(self.chain, False)

    def none(self):
        self.chain.append(Rule("be none", none, [], self.invert))
        return Validator(self.chain, False)

    def first(self, a):
        self.chain.append(Rule("contain first %s" % a, first, [a], self.invert))
        return Validator(self.chain, False)

    def last(self, a):
        self.chain.append(Rule("contain last %s" % a, last, [a], self.invert))
        return Validator(self.chain, False)

    def list_(self):
        self.chain.append(Rule("be a list", list_, [], self.invert))
        return Validator(self.chain, False)

    def bool_(self):
        self.chain.append(Rule("be a bool", bool_, [], self.invert))
        return Validator(self.chain, False)

    def less_than(self, a):
        self.chain.append(Rule("be less than %s" % a, less_than, [a], self.invert))
        return Validator(self.chain, False)

    def less_or_equal_than(self, a):
        self.chain.append(Rule("be less or equal than" % a, less_or_equal_than, [a], self.invert))
        return Validator(self.chain, False)

    def includes(self, a):
        self.chain.append(Rule("include %s" % a, includes, [a], self.invert))
        return Validator(self.chain, False)

    def positive(self):
        self.chain.append(Rule("be positive", positive, [], self.invert))
        return Validator(self.chain, False)

    def negative(self):
        self.chain.append(Rule("be negative", negative, [], self.invert))
        return Validator(self.chain, False)

    def empty(self):
        self.chain.append(Rule("be empty", empty, [], self.invert))
        return Validator(self.chain, False)

    def divisible_by(self, a):
        self.chain.append(Rule("be divisible by %s" % a, divisible_by, [a], self.invert))
        return Validator(self.chain, False)

    def float_(self, a):
        self.chain.append(Rule("be a float", float_, [a], self.invert))

    def dict_(self, a):
        self.chain.append(Rule("be a dict", dict_, [a], self.invert))

    def set_(self, a):
        self.chain.append(Rule("be a set", set_, [a], self.invert))

    def tuple_(self, a):
        self.chain.append(Rule("be a tuple", tuple_, [a], self.invert))

    def of_type(self, a):
        self.chain.append(Rule("of type %s" % a, of_type, [a], self.invert))

    def validate(self, value, value_name: str):
        error_message = "%s must:\n" % value_name
        should_raise_value_error = False
        for rule in self.chain:
            if not rule.test(value):
                error_message += "\t - %s" % rule.name
                should_raise_value_error = True
        if should_raise_value_error:
            raise ValueError(error_message)
