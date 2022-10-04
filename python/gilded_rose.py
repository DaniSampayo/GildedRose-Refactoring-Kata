# -*- coding: utf-8 -*-

from enum import Enum
from typing import List

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class Catalog(Enum):
    SULFURAS = "Sulfuras, Hand of Ragnaros"
    AGED = "Aged Brie"
    PASSES = "Backstage passes to a TAFKAL80ETC concert"
    LOWER_QUALITY = 0
    UPPER_QUALITY = 50
    LOWER_SELL_IN = 6
    UPPER_SELL_IN = 11
    
class GildedRose(object):

    def __init__(self, item_collection: List[Item]):
        self.item_collection = item_collection
    
    def _get_item_by_collection(self):
        
        return [item for item in self.item_collection]

    def _update_quality_by_name(self,
                        item_name: str,
                        item_quality: int):
        
        if item_name != Catalog.SULFURAS:
            item_quality = item_quality - 1
   
    def update_quality_by_lower_threshold(self,
                                        item_name: str,
                                       item_quality: int):
        if item_quality > Catalog.LOWER_QUALITY:
            self._update_quality_by_name(item_name,item_quality)
            
    def _update_quality_by_upper_threshold(self,
                                   item_quality: int):
        
        if item_quality < Catalog.UPPER_QUALITY:
            item_quality = item_quality + 1
    
    def _update_quality_by_sell(self,
                               item_sell_in: int,
                               item_quality: int):
        
        if item_sell_in < Catalog.UPPER_SELL_IN:
            self._update_quality_by_upper_threshold(item_quality)
        if item_sell_in < Catalog.LOWER_SELL_IN:
            self._update_quality_by_upper_threshold(item_quality)    
                       
    def _update_quality_by_threshold(self,
                        item_name: str,
                        item_sell_in: int,
                        item_quality: int):
        if item_name != Catalog.AGED and item_name != Catalog.PASSES:
            self.update_quality_by_lower_threshold(item_name,
                                                   item_quality)
        else:
            self._update_quality_by_upper_threshold(item_quality)
            if item_name == Catalog.PASSES:
                self._update_quality_by_sell(item_sell_in,
                                             item_quality)
                
    def _update_quality_by_sell_under_zero(self,
                                           item_sell_in: int,
                                           item_name: str,
                                           item_quality: int):
        if item_sell_in < 0:
            if item_name != Catalog.AGED and item_name != Catalog.PASSES:
                if item_quality > Catalog.LOWER_QUALITY:
                    self._update_quality_by_name(item_name,
                                                 item_quality)
                else:
                    item_quality = item_quality - item_quality
            else:
                self._update_quality_by_upper_threshold(item_quality)
                
    def update_quality(self):
        
        for item in self.item_collection:
            self._update_quality_by_threshold(item.name,
                                              item,item.quality,
                                              item.sell_in)
            self._update_quality_by_name(item.name,
                                         item.quality)
            self._update_quality_by_sell_under_zero(item.sell_in,
                                                    item.name,
                                                    item.quality)
