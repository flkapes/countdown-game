from main import *


def test_select_characters():
    assert type(select_characters()) == type('l')
    assert len(select_characters()) == 9


def test_dictionary_reader():
    assert type(dictionary_reader()) == type(['hi'])


def test_word_lookup():
    y, x = word_lookup(dictionary_reader(), select_characters())
    assert type(y) == type(['hi'])
    assert type(x) == type(['hi'])

