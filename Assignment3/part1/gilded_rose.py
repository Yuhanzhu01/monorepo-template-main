# -*- coding: utf-8 -*-


class Item:
    def __init__(self, name, sell_in, quality):
        """ DO NOT CHANGE THIS CLASS!!!"""
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class DefaultInventoryUpdate:
    @staticmethod
    def update(item):
        if item.sell_in >= 0:
            item.sell_in -= 1
            item.quality -= 1
        else:
            item.sell_in -= 1
            item.quality -= 2
        item.quality = max(0, item.quality)


class AgedBrieUpdate:
    @staticmethod
    def update(item):
        item.sell_in -= 1
        item.quality += 1
        item.quality = min(50, item.quality)


class SulfurasUpdate:
    @staticmethod
    def update(item):
        # Sulfuras stays the same
        pass


class BackstagePassesUpdate:
    @staticmethod
    def update(item):
        if item.sell_in > 10:
            item.quality += 1
        elif 5 < item.sell_in <= 10:
            item.quality += 2
        elif 0 < item.sell_in <= 5:
            item.quality += 3
        elif item.sell_in <= 0:
            item.quality = 0

        item.sell_in -= 1
        item.quality = min(50, item.quality)


class ConjuredUpdate:
    @staticmethod
    def update(item):
        if item.sell_in >= 0:
            item.sell_in -= 1
            item.quality -= 2
        else:
            item.sell_in -= 1
            item.quality -= 4
        item.quality = max(0, item.quality)


class GildedRose(object):
    def __init__(self, items):
        self.items = items
        self.update_allItems = {
            "Aged Brie": AgedBrieUpdate,
            "Sulfuras, Hand of Ragnaros": SulfurasUpdate,
            "Backstage passes to a TAFKAL80ETC concert": BackstagePassesUpdate,
            "Conjured Mana Cake": ConjuredUpdate,
        }

    def update_quality(self):
        for item in self.items:
            strategy = self.update_allItems.get(item.name, DefaultInventoryUpdate)
            strategy.update(item)


