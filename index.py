import sys

if sys.version_info[0] < 3:
    # To ensure that the program is executed using python 3
    raise Exception("Please run the program using Python 3")

from cli.cmd_parser import parse_command_line_arguments
from util import logger

try:
    parse_command_line_arguments()
except Exception as ex:
    logger.exception(ex)
