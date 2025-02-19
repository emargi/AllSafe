"""
    Test functions defined in allsafe/modules/utils.py
"""

from allsafe.modules.utils import (
    passwd_chars_filter, passwd_length_filter,
    get_passwd_score, PASSWORD_CHARACTERS,
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

def test_passwd_score():
    passwd1 = "abc123"
    score1 = 2 + (6-8)//2
    passwd2 = "AaBbCc123"
    score2 = 3 + (9-8)//2
    passwd3 = "AaBbCc123!@#"
    score3 = 4 + (12-8)//2

    assert get_passwd_score(passwd1, len(passwd1)) == score1
    assert get_passwd_score(passwd2, len(passwd2)) == score2
    assert get_passwd_score(passwd3, len(passwd3)) == score3
