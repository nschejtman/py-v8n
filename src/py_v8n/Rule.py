import types


class Rule:
    def __init__(self, name: str, fn: types.FunctionType, args: list, invert: bool, every: bool):
        self.name = name
        self.fn = fn
        self.args = args
        self.invert = invert
        self.every = every

    def test(self, value):
        if not self.every:
            return self._test_single_value(value)
        else:
            for elem in value:
                if not self._test_single_value(elem):
                    return False
            return True

    def _test_single_value(self, value):
        test_args = self.args.copy()
        test_args.insert(0, value)
        if not self.invert:
            return self.fn(test_args)
        else:
            return not self.fn(test_args)
