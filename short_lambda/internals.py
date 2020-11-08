
from operator import *


class NotDefinedType:
    pass
NotDefined = NotDefinedType()


class FClass:
    def __call__(self, fn):
        if isinstance(fn, XYAttr):
            return lambda x: getattr(x, fn.item)
        if isinstance(fn, XYObj):
            return lambda x: x
        if not callable(fn):
            raise Exception("Invalid short lambda")
        return fn


class XYAttr:
    def __init__(self, item):
        self.item = item

    def __call__(self, arg=NotDefined):
        if arg is NotDefined:
            return lambda x: getattr(x, self.item)()
        if isinstance(arg, XYObj):
            return lambda x, y: getattr(x, self.item)(y)
        return lambda x: getattr(x, self.item)(arg)


class XYObj:
    def _make_fn(self, other, op):
        if isinstance(other, XYObj):
            if self is other:
                return lambda x: op(x, x)
            return op
        return lambda x: op(x, other)

    def __getattr__(self, item):
        return XYAttr(item)

    def __call__(self, arg=NotDefined):
        if arg is NotDefined:
            return lambda x: x()
        return lambda x: x(arg)

    def __eq__(self, other):
        return self._make_fn(other, eq)

    def __ne__(self, other):
        return self._make_fn(other, ne)

    def __lt__(self, other):
        return self._make_fn(other, lt)

    def __gt__(self, other):
        return self._make_fn(other, gt)

    def __le__(self, other):
        return self._make_fn(other, le)

    def __ge__(self, other):
        return self._make_fn(other, ge)

    def __add__(self, other):
        return self._make_fn(other, add)

    def __sub__(self, other):
        return self._make_fn(other, sub)

    def __mul__(self, other):
        return self._make_fn(other, mul)

    def __truediv__(self, other):
        return self._make_fn(other, truediv)

    def __floordiv__(self, other):
        return self._make_fn(other, floordiv)
