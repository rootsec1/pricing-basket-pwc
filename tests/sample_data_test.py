import unittest

from data import sample_data


class SampleDataTest(unittest.TestCase):

    def test_mock_items(self):
        print("\nRunning SampleDataTest."+self._testMethodName)
        item_list = sample_data.get("items")
        self.assertEqual(len(item_list), 4)

    def test_mock_offers(self):
        print("\nRunning SampleDataTest."+self._testMethodName)
        offer_list = sample_data.get("offers")
        self.assertEqual(len(offer_list), 2)


if __name__ == "__main__":
    unittest.main()
