from fuel import convert, gauge
import pytest


def test_convert():
    assert convert("1/4") == 25
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("4/4") == 100


def test_gauge():
    assert gauge(2) == "2%"
    assert gauge(50) == "50%"
    assert gauge(98) == "98%"
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_alpha():
    with pytest.raises(ValueError):
        convert("cat/dog")
