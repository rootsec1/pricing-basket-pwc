from enum import Enum

class ItemName(Enum):
    SOUP = "SOUP"
    BREAD = "BREAD"
    MILK = "MILK"
    APPLES = "APPLES"

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))
