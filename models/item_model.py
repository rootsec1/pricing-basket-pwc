from uuid import UUID, uuid4
from dataclasses import dataclass, field

from constants.enums import ItemName, ItemUnit


@dataclass
class ItemModel:
    id: UUID = field(init=False)  # Unique identifier
    name: ItemName  # Enum of valid item names
    cost: float  # In pounds
    unit: ItemUnit  # Enum of valid units for the item

    def __post_init__(self):
        self.id = uuid4()  # Auto-generated field

    def __str__(self) -> str:
        return "{}: {} - {} pounds per {}".format(
            str(self.id),
            self.name,
            self.cost,
            self.unit
        )
