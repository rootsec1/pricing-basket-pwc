from uuid import UUID, uuid4
from dataclasses import dataclass, field

from constants.enums import ItemName, ItemUnit


@dataclass
class ItemModel:
    id: UUID = field(init=False)  # Auto-generated field
    name: ItemName
    cost: float  # In pounds
    unit: ItemUnit

    def __post_init__(self):
        self.id = uuid4()

    def __str__(self) -> str:
        return "{}: {} - {} pounds per {}".format(
            str(self.id),
            self.name,
            self.cost,
            self.unit
        )
