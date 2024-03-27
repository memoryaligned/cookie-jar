import argparse
import sys

from {{cookiecutter.repo_name}}.services.database import db_init


def _get_argparse(args):
    parser = argparse.ArgumentParser(prog="{{cookiecutter.repo_name}}")
    subparsers = parser.add_subparsers(help="available subcommands")

    # first sub-command
    db_parser = subparsers.add_parser("db", help="DB commands")
    db_parser.add_argument("-i", "--init", action="store_true")

    args = parser.parse_args(args)
    return args


def main():
    args = _get_argparse(sys.argv[1:])

    if "init" in args:
        db_init()
