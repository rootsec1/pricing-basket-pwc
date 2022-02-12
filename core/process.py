from typing import List
from collections import Counter
from datetime import datetime

from models import ItemModel, Offer
from data import mock_data
from constants import ItemName
from util import find_item_model_by_name, color_output

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
    subtotal = round(subtotal, 2)
    color_output("Subtotal: #{}".format(subtotal))
    return subtotal


def add_discount(master_offer: Offer):
    discount = round(
        master_offer.discount_percentage /
        100 * master_offer.offered_item.cost, 2
    )
    discount *= 100  # Convert pounds to pence
    color_output("{}: -{}p".format(master_offer.name, discount))
    return discount


def apply_offer(
    master_cart_counter: Counter,
    master_offer: Offer,
) -> float:
    offered_item: ItemModel = master_offer.offered_item
    if offered_item.name not in master_cart_counter:
        # No discount since the item is not present
        return 0

    master_prerequisite_item_list = master_offer.prerequisite_items
    master_prerequisite_item_name_list = list(map(
        lambda x: x.name,
        master_prerequisite_item_list
    ))

    temp_cart_counter = master_cart_counter.copy()
    temp_prerequisite_item_name_list = master_prerequisite_item_name_list.copy()

    discount_for_offer = 0

    for item_name_cart in temp_cart_counter:
        item_name_cart_count = temp_cart_counter[item_name_cart]

        # When the pre-requisite item required to be eligible for the offer is
        # the same as the item on which the offer is applied
        # Example: Apple should be in cart to avail 10% discount on the same
        if item_name_cart == offered_item.name and len(master_prerequisite_item_name_list) == 1:
            for _ in range(item_name_cart_count):
                discount = add_discount(master_offer)
                discount_for_offer += discount
            continue

        # When the pre-requisite items required to be eligible for the offer is
        # different from the item on which the offer is applied
        # Example: 2 tins of soup are required to apply a 50% discount on a loaf of bread
        for _ in range(item_name_cart_count):
            if len(temp_prerequisite_item_name_list) == 0 and \
                offered_item.name in temp_cart_counter and \
                    temp_cart_counter[offered_item.name] >= 1:
                discount = add_discount(master_offer)
                discount_for_offer += discount

                temp_cart_counter[offered_item.name] -= 1
                temp_prerequisite_item_name_list = master_prerequisite_item_name_list.copy()

            if item_name_cart in temp_prerequisite_item_name_list:
                temp_prerequisite_item_name_list.remove(item_name_cart)
                temp_cart_counter[item_name_cart] -= 1

    return discount_for_offer


def apply_eligible_offers(
    cart_counter: Counter,
    offer_dataset: List[Offer]
) -> float:
    # Return discount amount
    total_discount = 0
    for offer in offer_dataset:
        if offer.valid_from_timestamp <= datetime.now() <= offer.valid_to_timestamp:
            discount_for_offer = apply_offer(cart_counter, offer)
            total_discount += discount_for_offer
    return total_discount


def process_cart(cart: List[str]):
    cart = list(map(lambda x: ItemName(x), cart))
    cart_counter = Counter(cart)  # Dictionary of

    subtotal = compute_subtotal(cart_counter, item_dataset)
    total_discount = apply_eligible_offers(cart_counter, offer_dataset)
    total = round(subtotal - total_discount, 2)

    if total_discount == 0:
        color_output("(no offers available)")
    color_output("Total: #{}".format(total))
