import unittest

from collections import Counter

from constants import ItemName
from core import *


class TestProcessingLogic(unittest.TestCase):

    def test_subtotal_computation_logic(self):
        print("\nRunning TestProcessingLogic."+self._testMethodName)
        sample_space = [ItemName.APPLE, ItemName.MILK, ItemName.BREAD]
        sample_space_counter = Counter(sample_space)
        sample_space_subtotal = compute_subtotal(
            sample_space_counter,
            item_dataset
        )
        self.assertAlmostEqual(sample_space_subtotal, 3.1)

    def test_discount(self):
        print("\nRunning TestProcessingLogic."+self._testMethodName)
        sample_space = [ItemName.APPLE]
        sample_space_counter = Counter(sample_space)
        sample_space_subtotal = compute_subtotal(
            sample_space_counter,
            item_dataset
        )
        total_discount = apply_eligible_offers(
            sample_space_counter,
            offer_dataset
        )
        self.assertAlmostEqual(total_discount, 0.1)


if __name__ == "__main__":
    unittest.main()
