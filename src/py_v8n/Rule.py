import types


class Rule:
    def __init__(self, name: str, fn: types.FunctionType, args: list, invert: bool):
        self.name = name
        self.fn = fn
        self.args = args
        self.invert = invert

    def test(self, value):
        test_args = self.args.copy()
        test_args.insert(0, value)
        if not self.invert:
            return self.fn(test_args)
        else:
            return not self.fn(test_args)
