import argparse
import sys

from {{cookiecutter.repo_name}}.command.inference import submit_inference


def _get_argparse(args):
    parser = argparse.ArgumentParser(prog="{{cookiecutter.repo_name}}")
    subparsers = parser.add_subparsers(
            dest="subcommand",
            help="available subcommands",
        )

    # first sub-command
    db_parser = subparsers.add_parser(
            "inference",
            help="submit an inference request",
        )
    db_parser.add_argument("-s", "--server", action="store")
    db_parser.add_argument("-p", "--port", action="store")
    db_parser.add_argument("-j", "--json", action="store")

    args = parser.parse_args(args)
    return args


def main():
    args = _get_argparse(sys.argv[1:])

    if "inference" == args.subcommand:
        submit_inference(args)
