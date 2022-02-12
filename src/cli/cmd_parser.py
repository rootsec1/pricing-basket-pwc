import argparse

from src.core import process_cart

from src.constants import ARG_PARSER_DESCRIPTION, ItemName


def parse_command_line_arguments():
    arg_parser = argparse.ArgumentParser(description=ARG_PARSER_DESCRIPTION)
    arg_parser.add_argument(
        "--cart",
        nargs="+",
        default=[],
        choices=ItemName.list(),
        type=str.upper,
        help="List of items in the cart, could be any of : {}".format(
            ItemName.list()),
        required=True
    )
    cart = arg_parser.parse_args().cart
    response = process_cart(cart=cart)
    print(response)
