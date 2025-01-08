from allsafe.modules import encrypt
from allsafe.modules.encryption import PASSWORD_CHARACTERS


def test_password_generator():
    test_key = "test"
    test_app = "Battle.net"
    test_username = "unknown999"

    passwds = encrypt(test_key, test_app, test_username)
    for passwd in passwds:
        assert isinstance(passwd, str)
        for char in passwd:
            assert char in PASSWORD_CHARACTERS


def test_if_passwords_are_the_same():
    test_key = "test"
    test_app = "battle.net"
    test_username = "unknown999"

    args = (test_app, test_username)
    passwds1 = encrypt(test_key, *args)

    passwds2 = encrypt(test_key, *(i.upper() for i in args))

    assert passwds1 == passwds2
