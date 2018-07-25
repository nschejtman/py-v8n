from .Rule import Rule
from .rules import *


class Validator:
    def __init__(self, chain: list, invert: bool):
        self.invert = invert
        self.chain = chain

    def test(self, value):
        for rule in self.chain:
            if not rule.test(value):
                return False
        return True

    def not_(self):
        return Validator(self.chain, True)

    def greater_than(self, a):
        self.chain.append(Rule("greater_than", greater_than, [a], self.invert))
        return Validator(self.chain, False)

    def greater_or_equal_than(self, a):
        self.chain.append(Rule("greater_or_equal_than", greater_or_equal_than, [a], self.invert))
        return Validator(self.chain, False)

    def between(self, a, b):
        self.chain.append(Rule("between", between, [a, b], self.invert))
        return Validator(self.chain, False)

    def str_(self):
        self.chain.append(Rule("str", str_, [], self.invert))
        return Validator(self.chain, False)

    def int_(self):
        self.chain.append(Rule("int", int_, [], self.invert))
        return Validator(self.chain, False)

    def even(self):
        self.chain.append(Rule("even", even, [], self.invert))
        return Validator(self.chain, False)

    def odd(self):
        self.chain.append(Rule("odd", odd, [], self.invert))
        return Validator(self.chain, False)

    def equal(self, a):
        self.chain.append(Rule("equal", equal, [a], self.invert))
        return Validator(self.chain, False)

    def min_length(self, a):
        self.chain.append(Rule("min_length", min_length, [a], self.invert))
        return Validator(self.chain, False)

    def max_length(self, a):
        self.chain.append(Rule("max_length", max_length, [a], self.invert))
        return Validator(self.chain, False)

    def length(self, a):
        self.chain.append(Rule("length", length, [a], self.invert))
        return Validator(self.chain, False)

    def none(self):
        self.chain.append(Rule("none", none, [], self.invert))
        return Validator(self.chain, False)

    def first(self, a):
        self.chain.append(Rule("first", first, [a], self.invert))
        return Validator(self.chain, False)

    def last(self, a):
        self.chain.append(Rule("last", last, [a], self.invert))
        return Validator(self.chain, False)

    def list_(self):
        self.chain.append(Rule("list", list_, [], self.invert))
        return Validator(self.chain, False)

    def bool_(self):
        self.chain.append(Rule("bool", bool_, [], self.invert))
        return Validator(self.chain, False)

    def less_than(self, a):
        self.chain.append(Rule("less_than", less_than, [a], self.invert))
        return Validator(self.chain, False)

    def less_or_equal_than(self, a):
        self.chain.append(Rule("less_or_equal_than", less_or_equal_than, [a], self.invert))
        return Validator(self.chain, False)

    def includes(self, a):
        self.chain.append(Rule("includes", includes, [a], self.invert))
        return Validator(self.chain, False)

    def positive(self):
        self.chain.append(Rule("positive", positive, [], self.invert))
        return Validator(self.chain, False)

    def negative(self):
        self.chain.append(Rule("negative", negative, [], self.invert))
        return Validator(self.chain, False)

    def empty(self):
        self.chain.append(Rule("empty", empty, [], self.invert))
        return Validator(self.chain, False)

    def divisible_by(self, a):
        self.chain.append(Rule("divisible_by", divisible_by, [a], self.invert))
        return Validator(self.chain, False)
