
from short_lambda import *

def test_F_X():
    assert F(X == 2)(2)
    assert not F(X == 2)(3)
    assert F(X != 2)(3)
    assert F(X == 2)(2)
    assert F(X < 2)(0)
    assert not F(X < 2)(2)
    assert F(X > 2)(3)
    assert not F(X > 2)(2)
    assert F(X <= 2)(2)
    assert not F(X <= 2)(3)
    assert F(X >= 2)(2)
    assert not F(X >= 2)(1)
    assert F(X + 2)(3) == 5
    assert F(X - 2)(3) == 1
    assert F(X * 3)(4) == 12
    assert F(X / 3)(5) == (5 / 3)
    assert F(X // 3)(5) == 1


def test_F_XY():
    assert F(X == Y)(1, 1)
    assert not F(X == Y)(1, 2)
    assert F(X != Y)(1, 2)
    assert not F(X != Y)(2, 2)
    assert F(X < Y)(2, 3)
    assert not F(X < Y)(3, 2)
    assert F(X > Y)(3, 2)
    assert not F(X > Y)(2, 3)
    assert F(X <= Y)(2, 2)
    assert F(X <= Y)(2, 3)
    assert not F(X <= Y)(3, 2)
    assert F(X >= Y)(2, 2)
    assert F(X >= Y)(3, 2)
    assert not F(X >= Y)(2, 3)
    assert F(X + Y)(2, 3) == 5
    assert F(X - Y)(5, 2) == 3
    assert F(X * Y)(10, 12) == 120
    assert F(X / Y)(3, 4) == (3 / 4)
    assert F(X // Y)(4, 3) == 1


def test_F_XX():
    assert F(X == X)(1)
    assert not F(X != X)(1)
    assert not F(X > X)(1)
    assert not F(X < X)(1)
    assert F(X >= X)(1)
    assert F(X <= X)(1)
    assert F(X + X)(3) == 6
    assert F(X - X)(5) == 0
    assert F(X * X)(5) == 25
    assert F(X / X)(4) == 1
    assert F(X // X)(3) == 1


def test_F_Attr():
    class T:
        def __init__(self, x):
            self.x = x

    assert F(X)(42) == 42
    assert F(X())(lambda: 4) == 4
    assert F(X(3))(lambda x: x + 5) == 8
    assert F(X.x)(T(1)) == 1
    assert F(X.x())(T(lambda: 2)) == 2
    assert F(X.x(4))(T(lambda x: x + 3)) == 7
