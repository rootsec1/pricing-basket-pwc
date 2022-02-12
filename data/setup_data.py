import json

from datetime import datetime
from typing import List, Tuple

from constants.enums import ItemName, ItemUnit
from models import ItemModel, Offer
from util import find_item_model_by_name


sample_data = json.load(open("./data/sample_data.json"))


def mock_items() -> List[ItemModel]:
    item_list = sample_data.get("items")
    for idx, item in enumerate(item_list):
        name = item.get("name")
        cost = item.get("cost")
        unit = item.get("unit")

        # Transformations
        name_in_enum = ItemName(name)
        unit_in_enum = ItemUnit(unit)
        item = ItemModel(
            name=name_in_enum,
            cost=cost,
            unit=unit_in_enum
        )
        item_list[idx] = item
    return item_list


def mock_offers(item_list: List[ItemModel]) -> List[Offer]:
    offer_list = sample_data.get("offers")
    for idx, offer in enumerate(offer_list):
        offered_item = offer.get("offered_item")
        discount_percentage = offer.get("discount_percentage")
        valid_from_timestamp = offer.get("valid_from_timestamp")
        valid_to_timestamp = offer.get("valid_to_timestamp")
        name = offer.get("name")
        prerequisite_items = offer.get("prerequisite_items")

        # Transformations
        offered_item = find_item_model_by_name(
            name=ItemName(offered_item),
            item_list=item_list
        )
        prerequisite_items = list(
            map(
                lambda x: find_item_model_by_name(
                    name=ItemName(x),
                    item_list=item_list
                ),
                prerequisite_items
            )
        )
        valid_from_timestamp = datetime.fromisoformat(valid_from_timestamp)
        valid_to_timestamp = datetime.fromisoformat(valid_to_timestamp)
        offer = Offer(
            offered_item=offered_item,
            discount_percentage=discount_percentage,
            valid_from_timestamp=valid_from_timestamp,
            valid_to_timestamp=valid_to_timestamp,
            name=name,
            prerequisite_items=prerequisite_items
        )
        offer_list[idx] = offer
    return offer_list


def mock_data() -> Tuple[List[ItemModel], List[Offer]]:
    fake_items = mock_items()
    fake_offers = mock_offers(item_list=fake_items)
    return fake_items, fake_offers
