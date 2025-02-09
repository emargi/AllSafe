"""
    Test functions defined in allsafe/modules/utils.py
"""
from allsafe.modules.utils import (
    passwd_chars_filter, passwd_length_filter,
    PASSWORD_CHARACTERS,
)


def test_passwd_chars_filter():
    test_chars1 = "acdbef"
    test_chars2 = ""
    test_chars3 = "aacc"
    test_chars4 = "a"

    assert passwd_chars_filter(test_chars1) == "abcdef"
    assert passwd_chars_filter(test_chars2) == PASSWORD_CHARACTERS
    try:
        passwd_chars_filter(test_chars3)
    except ValueError:
        pass
    else:
        raise Exception

    try:
        passwd_chars_filter(test_chars4)
    except ValueError:
        pass
    else:
        raise Exception

def test_passwd_length_filter():
    test_length1 = "5"
    test_length2 = "a"
    test_length3 = ""

    assert passwd_length_filter(test_length1) == int(test_length1)
    try:
        passwd_length_filter(test_length2)
    except ValueError:
        pass
    else:
        raise Exception

    try:
        passwd_length_filter(test_length3)
    except ValueError:
        pass
    else:
        raise Exception
