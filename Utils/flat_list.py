import functools
import operator


def flat(a):
    return functools.reduce(operator.iconcat, a, [])
