import argparse

from src.constants.descriptive_strings import ARG_PARSER_DESCRIPTION
from src.constants.enums import ItemName

def parse_command_line_arguments():
    arg_parser = argparse.ArgumentParser(description=ARG_PARSER_DESCRIPTION)
    arg_parser.add_argument(
        "--cart",
        nargs="+",
        default=[],
        choices=ItemName.list(),
        type=str.upper,
        help="List of items in the cart, could be any of : {}".format(ItemName.list()),
        required=True
    )
    cart = arg_parser.parse_args().cart
    
