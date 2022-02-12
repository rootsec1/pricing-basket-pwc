from typing import List
from collections import Counter
from datetime import datetime

from models import ItemModel, Offer
from data import mock_data
from constants import ItemName
from util import find_item_model_by_name, color_output, logger

# Mocking the data, list of items and list of offers come from a sample JSON
# In the real world, this layer could be modified to query a database or an API
item_dataset, offer_dataset = mock_data()


def compute_subtotal(cart_counter: Counter, item_dataset: List[ItemModel]) -> float:
    # Compute total before discounts
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
    # Check if cart is eligible for individual offer
    offered_item: ItemModel = master_offer.offered_item
    if offered_item.name not in master_cart_counter:
        # No discount since the item is not present
        return 0

    # List of item names that should be in cart to be eligible for this offer
    master_prerequisite_item_name_list = list(map(
        lambda x: x.name,
        master_offer.prerequisite_items
    ))

    # Temporary variables that get reset each time an offer is applied
    # Will come into play when the same offer can be applied multiple times
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
                # Reset temporary variable after applying the offer
                temp_prerequisite_item_name_list = master_prerequisite_item_name_list.copy()

            if item_name_cart in temp_prerequisite_item_name_list:
                # Ensuring that quantity of pre requisite items required are present in cart
                # Example: 2 tins of soup are required to apply a 50% discount on a loaf of bread
                temp_prerequisite_item_name_list.remove(item_name_cart)
                temp_cart_counter[item_name_cart] -= 1

    return discount_for_offer


# Check for all eligible offers
def apply_eligible_offers(
    cart_counter: Counter,
    offer_dataset: List[Offer]
) -> float:
    # Return total discount amount for all applied offers
    total_discount = 0
    for offer in offer_dataset:
        if offer.valid_from_timestamp <= datetime.now() <= offer.valid_to_timestamp:
            # Ensuring that the offer is still valid
            discount_for_offer = apply_offer(cart_counter, offer)
            total_discount += discount_for_offer
    return total_discount


def process_cart(cart: List[str]) -> None:
    try:
        cart: List[ItemName] = list(map(lambda x: ItemName(x), cart))
        # Dictionary of item names and their respective quantity in cart
        # Example: {'SOUP': 3, 'BREAD': 1, 'APPLE': 1}
        cart_counter: Counter = Counter(cart)

        subtotal: float = compute_subtotal(cart_counter, item_dataset)
        total_discount: float = apply_eligible_offers(
            cart_counter,
            offer_dataset
        )
        total: float = round(subtotal - total_discount, 2)

        if total_discount == 0:  # No offers were eligible for the cart
            color_output("(no offers available)")
        color_output("Total: #{}".format(total))
    except Exception as ex:
        logger.exception("Processing logic exception: "+str(ex))
