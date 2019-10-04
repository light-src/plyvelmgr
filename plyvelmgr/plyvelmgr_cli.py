import sys
import argparse
from .commands.command_erasebykey import CommandEraseKey
from .commands.command_setbykey import CommandSetByKey
from .commands.command_getbykey import CommandGetByKey
from .commands.command_checkdiff import CommandCheckDiff


def main():
    handlers = [
        CommandSetByKey,
        CommandEraseKey,
        CommandGetByKey,
        CommandCheckDiff
    ]

    parser = argparse.ArgumentParser(
        prog='dbsetter'
    )

    sub_parser = parser.add_subparsers(title='subcommands')
    common_parser = create_common_parser()

    for handler in handlers:
        handler(sub_parser, common_parser=common_parser)

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        return 1

    args = parser.parse_args()
    args.func(args)

    return 0


def create_common_parser() -> argparse.ArgumentParser:

    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser.add_argument(
        "--db",
        type=str,
        required=True,
    )

    return parent_parser
