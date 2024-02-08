from um import count

def test_correct_inputs():
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2
    assert count("Um, hello world!") == 1
    assert count("...um?") == 1
    assert count("um, um, um") == 3
    assert count("um!Um") == 2

def test_bad_inputs():
    assert count("") == 0
    assert count("yum") == 0
    assert count("umum") == 0
    assert count("") == 0

def test_non_characters():
    assert count("123") == 0
    assert count("1um") == 0
    assert count("um2") == 0
    assert count("_um") == 0
    assert count("um_") == 0

'''
def test_only_space():
    assert count("Um, hello, um world") == 1
'''
