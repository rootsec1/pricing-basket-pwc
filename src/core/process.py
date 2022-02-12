from typing import List
from collections import Counter

from src.models import ItemModel
from src.data import mock_data
from src.constants import ItemName
from src.util import find_item_model_by_name

item_dataset, offer_dataset = mock_data()


def compute_subtotal(cart_counter: Counter, item_dataset: List[ItemModel]) -> float:
    subtotal = 0
    for cart_item in cart_counter:
        item: ItemModel = find_item_model_by_name(
            name=cart_item,
            item_list=item_dataset
        )
        # subtotal for item = cost of item * quantity of same in cart
        subtotal += item.cost * cart_counter.get(cart_item)
    return round(subtotal, 2)


def process_cart(cart: List[str]) -> str:
    cart = list(map(lambda x: ItemName(x), cart))
    cart_counter = Counter(cart)  # Dictionary of

    subtotal = compute_subtotal(cart_counter, item_dataset)
    print(subtotal)

    response_text = ""
    return response_text
