from typing import List
from src.constants import ItemName
from src.models import ItemModel


def find_item_model_by_name(name: ItemName, item_list: List[ItemModel]) -> ItemModel:
    return next(item for item in item_list if item.name == name)
