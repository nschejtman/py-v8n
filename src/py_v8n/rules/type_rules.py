def of_type(args):
    return type(args[0]) == args[1]


def list_(args):
    return of_type([args[0], list])


def bool_(args):
    return of_type([args[0], bool])


def str_(args):
    return of_type([args[0], str])


def int_(args):
    return of_type([args[0], int])


def tuple_(args):
    return of_type([args[0], tuple])


def float_(args):
    return of_type([args[0], float])


def dict_(args):
    return of_type([args[0], dict])


def set_(args):
    return of_type([args[0], set])
