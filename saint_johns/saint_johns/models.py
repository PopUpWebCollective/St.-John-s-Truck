"""Models for St. John's Truck & Engine Website

Parts, Manufacturer, Classes (tables) to support search function on Parts page

"""

from django.db import models


class Part(models.Model):
    """identifier and details for individual part sold"""

    stock = models.CharField()  # aka Part Number
    list_price = models.FloatField()  # Decimal is unnecessary for this object
    manufacturer = models.CharField()  # aka Part Make
    condition = models.CharField()
    description = models.TextField()  # can this be CharField?
    # part_type = parts_by_number - where did this tag come from and why?
    # what about classification of part (transmission, axle, etc?)

    def __str__(self):
        """readable output of object fields"""
        return 'Part_str({}, {}, {}, {}, {}, {})'.format(
            self.id,
            self.stock,
            self.list_price,
            self.manufacturer,
            self.condition,
            self.description
        )  # should this be rewritten before deployment?

    def __repr__(self):
        """readable output of object fields"""
        return 'Part_repr({!r}, {!r}, {!r}, {!r}, {!r}, {!r})'.format(
            self.id,
            self.stock,
            self.list_price,
            self.manufacturer,
            self.condition,
            self.description
        )
