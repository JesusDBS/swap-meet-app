import pytest
from app.vendor import Vendor
from app.item import Item
from app.clothing import Clothing
from app.decor import Decor
from app.electronics import Electronics


def test_items_have_have_age_attribute_default_zero():
    item = Item()
    clothes = Clothing()
    decor = Decor()
    electronics = Electronics()

    assert item.age == 0
    assert clothes.age == 0
    assert decor.age == 0
    assert electronics.age == 0


def test_swap_by_newest():
    pass


