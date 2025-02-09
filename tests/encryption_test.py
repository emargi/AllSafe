"""
    Test functions defined in allsafe/modules/encryption.py
"""

from allsafe.modules import generate_passwd
from allsafe.modules.encryption import add_ords
from allsafe.modules.utils import PASSWORD_CHARACTERS


default_kwargs = {
    "lengths": (8, 16, 24),
    "passwd_chars": PASSWORD_CHARACTERS,
}

def test_password_generator():
    """Test the functionality"""
    test_key = "test"
    test_app = "Battle.net"
    test_username = "unknown999"

    passwds = generate_passwd(test_key, test_app, test_username, **default_kwargs)
    for passwd in passwds:
        assert isinstance(passwd, str)
        for char in passwd:
            assert char in PASSWORD_CHARACTERS


def test_if_passwords_are_the_same():
    """
    Test if the function returns the same password
    if the given data are the same but uppercase
    (except for the key, of course)
    """
    test_key = "test"
    test_app = "battle.net"
    test_username = "unknown999"

    args = (test_app, test_username)
    passwds1 = generate_passwd(test_key, *args, **default_kwargs)

    passwds2 = generate_passwd(test_key, *(i.upper() for i in args),
                               **default_kwargs)

    assert passwds1 == passwds2

def test_password_lengths():
    """
    Test if the function respects the given lengths
    """
    test_key = "test"
    test_app = "battle.net"
    test_username = "unknown999"
    test_lengths = [2, 5, 8, 19, 24, 44, 62, 63]
    passwds = generate_passwd(
        test_key, test_app, test_username,
        lengths=test_lengths,
        passwd_chars=PASSWORD_CHARACTERS
    )
    for index, passwd in enumerate(passwds):
        assert len(passwd) == test_lengths[index]

def test_password_chars():
    """
    Test if the function respects the given characters
    """
    test_key = "test"
    test_app = "battle.net"
    test_username = "unknown999"
    test_lengths = [2, 5, 8, 19, 24, 44, 62, 63]
    test_chars = "abc123"
    passwds = generate_passwd(
        test_key, test_app, test_username,
        lengths=test_lengths, passwd_chars=test_chars
    )
    for index, passwd in enumerate(passwds):
        assert len(passwd) == test_lengths[index]
        for char in passwd:
            assert char in test_chars

def test_add_ords():
    """
    Test add_ords's functionality
    """
    ords1 = [1, 2, 3, 4, 5, 6, 7]
    ords2 = [3, 6, 9]

    new_ords = add_ords(ords1, ords2)
    expected_ords = [
        1+3, 2+6, 3+9,
        4+3, 5+6, 6+9,
        7+3,
    ]
    assert new_ords == expected_ords
