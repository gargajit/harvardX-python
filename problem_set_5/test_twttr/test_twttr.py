from twttr import shorten

def test_starts_with_vowel():
    assert shorten("apple") == "ppl"
    assert shorten("One") == "n"
    assert shorten("EAGLE") == "GL"

def test_starts_wth_consonant():
    assert shorten("cat") == "ct"
    assert shorten("Twitter") == "Twttr"

def test_alphanumeric():
    assert shorten("1") == "1"
    assert shorten(".") == "."
