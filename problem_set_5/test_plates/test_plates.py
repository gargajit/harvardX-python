from plates import is_valid

def test_start_num():
    assert is_valid("A100") == False
    assert is_valid("1A") == False
    assert is_valid("11ABCD") == False

def test_start_alpha():
    assert is_valid("CS") == True
    assert is_valid("CSGO11") == True

def test_bad_range():
    assert is_valid("C") == False
    assert is_valid("GOODBYE") == False
    assert is_valid("CS50000") == False

def test_all_alpha():
    assert is_valid("HELLO") == True

def test_rest_num():
    assert is_valid("CS5000") == True

def test_first_num_zero():
    assert is_valid("CS05") == False

def test_no_alpha_after_num():
    assert is_valid("CS50X") == False

def test_non_alnum():
    assert is_valid("CS 50") == False
    assert is_valid("CS50-1") == False
    assert is_valid("CS,HAR") == False
