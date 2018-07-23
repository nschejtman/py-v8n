class Rule:
    def __init__(self, name: str, fn: function, args: list, invert: bool):
        self.name = name
        self.fn = fn
        self.args = args
        self.invert = invert

    def test(self, value):
        if not self.invert:
            return self.fn(value, self.args)
        else:
            return not self.fn(value, self.args)
