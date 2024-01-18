from bank import value

def test_Hello():
    assert value("Hello") == 0
    assert value("hello") == 0
    assert value("hello, world") == 0

def test_Hi():
    assert value("Hi") == 20
    assert value("hi") == 20
    assert value("Hi, World    ") == 20


def test_others():
    assert value("Welcome!") == 100
    assert value("What's up?") == 100
    assert value("What's happening?") == 100
