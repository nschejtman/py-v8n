def greater_than(args):
    return args[0] > args[1]


def greater_or_equal_than(args):
    return args[0] >= args[1]


def between(args):
    return args[1] <= args[0] <= args[2]


def even(args):
    return divisible_by([args[0], 2])


def odd(args):
    return args[0] % 2 != 0


def equal(args):
    return args[0] == args[1]


def min_length(args):
    return len(args[0]) >= args[1]


def max_length(args):
    return len(args[0]) <= args[1]


def length(args):
    return len(args[0]) == args[1]


def none(args):
    return args[0] is None


def first(args):
    return args[0][0] == args[1]


def last(args):
    last_idx = len(args[0]) - 1
    return args[0][last_idx] == args[1]


def less_than(args):
    return args[0] < args[1]


def less_or_equal_than(args):
    return args[0] <= args[1]


def includes(args):
    return args[1] in args[0]


def positive(args):
    return greater_or_equal_than([args[0], 0])


def negative(args):
    return less_than([args[0], 0])


def empty(args):
    return length([args[0], 0])


def divisible_by(args):
    return args[0] % args[1] == 0
