# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class TestGildedRose(unittest.TestCase):
    def test_default_inventory_update(self):
        item = Item("Default Item", 5, 10)
        GildedRose([item]).update_quality()
        self.assertEqual(item.sell_in, 4)
        self.assertEqual(item.quality, 9)

    def test_aged_brie_update(self):
        item = Item("Aged Brie", 5, 10)
        GildedRose([item]).update_quality()
        self.assertEqual(item.sell_in, 4)
        self.assertEqual(item.quality, 11)

    def test_sulfuras_update(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 10)
        GildedRose([item]).update_quality()
        self.assertEqual(item.sell_in, 5)
        self.assertEqual(item.quality, 10)

    def test_backstage_passes_update(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 11, 10)
        GildedRose([item]).update_quality()
        self.assertEqual(item.sell_in, 10)
        self.assertEqual(item.quality, 11)

        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 10)
        GildedRose([item]).update_quality()
        self.assertEqual(item.sell_in, 4)
        self.assertEqual(item.quality, 13)

        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 10)
        GildedRose([item]).update_quality()
        self.assertEqual(item.sell_in, -1)
        self.assertEqual(item.quality, 0)

    def test_conjured_update(self):
        item = Item("Conjured Mana Cake", 5, 10)
        GildedRose([item]).update_quality()
        self.assertEqual(item.sell_in, 4)
        self.assertEqual(item.quality, 8)

    def test_unknown_item_update(self):
        item = Item("Unknown Item", 5, 10)
        GildedRose([item]).update_quality()
        self.assertEqual(item.sell_in, 4)
        self.assertEqual(item.quality, 9)


if __name__ == '__main__':
    unittest.main()
