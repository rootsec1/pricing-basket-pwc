from typing import List
from constants import ItemName, CBOLD, CEND, CWHITE, CRED
from models import ItemModel
from logging import Logger

logger = Logger(name="price-basket")


def find_item_model_by_name(name: ItemName, item_list: List[ItemModel]) -> ItemModel:
    # Map item name coming as input to an Item model instance
    return next(item for item in item_list if item.name == name)


def color_output(s: str) -> str:  # To color the output on the console
    try:
        colon_index = s.index(":")
        pre_colon_string = s[:colon_index+1]
        post_colon_string = s[colon_index+1:]
        print(pre_colon_string + CWHITE + CBOLD + post_colon_string + CEND)
    except ValueError:  # For strings that do not contain ":"
        print(CRED + s + CEND)
