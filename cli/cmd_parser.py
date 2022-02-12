import argparse

from typing import List
from core import process_cart

from constants import ARG_PARSER_DESCRIPTION, ItemName


def parse_command_line_arguments():
    arg_parser = argparse.ArgumentParser(description=ARG_PARSER_DESCRIPTION)
    arg_parser.add_argument(
        "--cart",
        nargs="+",  # To ensure that there is at least 1 item in the cart
        default=[],
        choices=ItemName.list(),  # Enum for choices
        type=str.upper,
        help="List of items in the cart, could be any of : {}".format(
            ItemName.list()
        ),
        required=True
    )
    cart: List[str] = arg_parser.parse_args().cart
    process_cart(cart=cart)
