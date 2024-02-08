from working import convert
import pytest

def test_correct_format():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10:00 PM to 5:50 AM") == "22:00 to 05:50"
    assert convert("10:30 AM to 8:50 PM") == "10:30 to 20:50"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("6:01 AM to 1:10 PM") == "06:01 to 13:10"


def test_wrong_format():
    with pytest.raises(ValueError):
        convert("10:7 AM - 5:1 PM")
    with pytest.raises(ValueError):
        convert("10:70 AM to 15:10 PM")
    with pytest.raises(ValueError):
        convert(":15 PM to 5:15 AM")
    with pytest.raises(ValueError):
        convert("10AM to 5PM")
    with pytest.raises(ValueError):
        convert("8:60 AM to 5:60 PM")


def test_wrong_inputs():
    with pytest.raises(ValueError):
        convert("10 AM")
    with pytest.raises(ValueError):
        convert("to 5:30 PM")
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert("25 AM - 200 PM")
