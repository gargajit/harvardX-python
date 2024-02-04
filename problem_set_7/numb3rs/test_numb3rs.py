from numb3rs import validate
import pytest

def test_correct_ips():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.1") == True
    assert validate("127.0.255.0") == True

def test_wrong_ips():
    assert validate("512.0.0.1") == False
    assert validate("0.512.0.1") == False
    assert validate("0.0.512.1") == False
    assert validate("0.0.0.1000") == False

def test_wrong_values():
    assert validate("cat") == False
    assert validate("1...2") == False
    assert validate("10.10.10.10.10") == False
