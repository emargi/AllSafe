import sys
import argparse

from allsafe.modules import ConsoleStream, generate_passwds, utils


__version__ = "1.5.1"

def print_passwds(console: ConsoleStream, passwds: list):
    for passwd in passwds:
        length = len(passwd)
        score = utils.get_passwd_score(passwd, length)
        emoji = utils.get_meaningful_emoji(score)
        # markdown representation
        md_passwd = console.styles.passwd(passwd)
        console.write(
            f"{emoji} {length}-Length Password:\t{md_passwd}"
        )

# ---------------------------
# Interactive mode functions
# ---------------------------
def handle_inputs(console: ConsoleStream):
    addr_sample = console.styles.gray("(e.g Battle.net)")
    addr = console.ask(f"Enter app address/name {addr_sample}")

    username_sample = console.styles.gray("(e.g user123)")
    username = console.ask(f"Enter username {username_sample}")

    case_note = console.styles.gray("(case-sensitive)")
    note = "(do [bold]NOT[/bold] forget this), " + case_note
    secret_key = console.ask(f"Enter secret key {note}")

    return (secret_key, addr, username)

def handle_custom_inputs(console: ConsoleStream):
    length_note = console.styles.gray("(between 4-64)")
    length = console.ask(f"Enter the length {length_note}",
                         func=utils.passwd_length_filter)

    chars_note = console.styles.gray("(enter for default)")
    chars = console.ask(f"Enter password characters {chars_note}",
                        func=utils.passwd_chars_filter)

    return (length, chars)

def run_interactive_mode(console: ConsoleStream):
    description = (
        "Get unique password for every app. No need to remeber all of them.\n"
        "No data stored and no internet needed. Use it before every sign-in."
    )
    console.panel("[bold]AllSafe[/bold] Modern Password Generator",
                  description, style=console.styles.GRAY)
    console.write(":link: Github: https://github.com/emargi/allsafe")
    console.write(":gear: Version: " + __version__ + "\n")

    args = handle_inputs(console)
    kwargs = {
        "lengths": utils.PASSWORD_LENGTHS,
        "passwd_chars": utils.PASSWORD_CHARACTERS
    }
    passwds = generate_passwds(*args, **kwargs)
    print_passwds(console, passwds)

    want_custom_passwd = console.ask(
        "Do you want a custom password?",
        choices=["y", "n"],
        default="n",
        show_default=False,
        case_sensitive=False,
    )
    if want_custom_passwd == "n":
        return

    length, chars = handle_custom_inputs(console)
    passwds = generate_passwds(*args, lengths=(length,), passwd_chars=chars)
    print_passwds(console, passwds)

# -----------------------------
# Non-Interactive mode functions
# -----------------------------
def parse_args(argv):
    usage = (
        "allsafe [-h] [-i] -a APP -u USERNAME -s SECRET "
        "[-l LENGTH] [-c CHARACTERS]"
    )
    parser = argparse.ArgumentParser(
        "AllSafe", usage,
    )
    # arguments
    parser.add_argument(
        "-i", "--interactive", type=bool, required=False,
        help="enter interactive mode",
    )
    parser.add_argument(
        "-a", "--app", type=str, required=True,
        help="Application name or url",
    )
    parser.add_argument(
        "-u", "--username", type=str, required=True,
        help="Your username or something unique to you",
    )
    parser.add_argument(
        "-s", "--secret", type=str, required=True,
        help="Your secret key to this password (case-sensitive)",
    )
    parser.add_argument(
        "-l", "--length", type=int, required=False,
        help="Password length, (default: 8, 16, 24)",
    )
    parser.add_argument(
        "-c", "--characters", type=str, required=False,
        help="Password characters",
    )

    return parser.parse_args(argv)

def run_non_interactive_mode(console: ConsoleStream, args):
    secret = args.secret
    app = args.app.lower()
    username = args.username.lower()
    chars = utils.passwd_chars_filter(args.characters)
    if args.length:
        length = utils.passwd_length_filter(args.length)
        lengths = (length,)
    else:
        lengths = utils.PASSWORD_LENGTHS

    passwds = generate_passwds(
        secret, app, username,
        lengths=lengths,
        passwd_chars=chars,
    )
    print_passwds(console, passwds)

# --------------
# main function
# --------------
def main():
    console = ConsoleStream()
    argv = sys.argv[1:]
    if len(argv) == 0 or "-i" in argv:
        try:
            run_interactive_mode(console)
        except KeyboardInterrupt:
            pass
        return

    args = parse_args(argv)
    try:
        run_non_interactive_mode(console, args)
    except ValueError as e:
        console.error(e)


if __name__ == "__main__":
    main()
