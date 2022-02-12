# TODO: Type Hinting
# TODO: Unit Tests
# TODO: Logging
# TODO: Comments for code
# TODO: DS/Algo
# TODO: Directory and code structure
# TODO: Error handling

import sys

from cli.cmd_parser import parse_command_line_arguments

if sys.version_info[0] < 3:
    # To ensure that the program is executed using python 3
    raise Exception("Please run the program using Python 3")
else:
    parse_command_line_arguments()
