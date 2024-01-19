import argparse

# from {{cookiecutter.repo_name}}.command.ACTION import callback_fn


def _get_argparse():
    parser = argparse.ArgumentParser(prog="{{cookiecutter.repo_name}}")
    subparsers = parser.add_subparsers(help="available subcommands")

    # first sub-command
    # ACTION_parser = subparsers.add_parser("ACTION", help="ACTION commands")
    # ACTION_parser.add_argument("-s", "--summary", action="store_true")

    args = parser.parse_args()
    return args


def main():
    args = _get_argparse()

    # if "ACTION" in args and arg.ACTION:
    #     callback_fn()
