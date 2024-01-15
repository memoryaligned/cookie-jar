import argparse

from {{cookiecutter.project_name}}.cmd.list import cmd_list


def _get_argparse():
    parser = argparse.ArgumentParser(prog="{{cookiecutter.project_name}}")

    subparsers = parser.add_subparsers(help="available subcommands")

    admin_parser = subparsers.add_parser("mq", help="MQ Commands")
    admin_parser.add_argument(
        "-l", "--list", help="list messages in the topic")

    args = parser.parse_args()
    return args


def main():
    args = _get_argparse()

    if "list" in args and args.list:
        cmd_list(args.list)
