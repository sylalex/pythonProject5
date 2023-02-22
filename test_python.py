import math

lst = [1, 3, 2]
def filter_too(p):
    if p > 2:
        return True
    else:
        return False


def test_filter():
    assert list(filter(filter_too, lst)) == [3]

def test_float():
    assert list(map(float, lst)) == [1.0, 3.0, 2.0]

def test_sort():
    assert sorted(lst) == [1, 2, 3]


def test_pi():
    assert math.pi == 3.141592653589793


def test_sqrt():
    assert math.sqrt(4) == 2


def test_pow():
    assert math.pow(4, 2) == 16


def test_hypot():
    assert math.hypot(4, 3) == 5
