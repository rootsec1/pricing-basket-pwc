from uuid import UUID, uuid4
from dataclasses import dataclass, field
from typing import Optional, List
from datetime import datetime

from .item_model import ItemModel


@dataclass
class Offer:
    id: UUID = field(init=False)  # Unique identifier

    # Required
    offered_item: ItemModel  # Item offered upon discount
    discount_percentage: float
    # Offer validity duration
    valid_from_timestamp: datetime
    valid_to_timestamp: datetime

    # Description/name of the offer
    name: Optional[str] = field(default_factory=list)
    prerequisite_items: Optional[List[ItemModel]] = field(
        default_factory=list
    )  # Items to have in cart to be eligible for offer

    def __post_init__(self):
        self.id = uuid4()  # Auto-generated field

    def __str__(self) -> str:
        return "{}: {} - {} - {} - {}, from {} to {}".format(
            str(self.id),
            str(self.offered_item),
            self.discount_percentage,
            self.name,
            str(self.prerequisite_items),
            str(self.valid_from_timestamp),
            str(self.valid_to_timestamp)
        )
