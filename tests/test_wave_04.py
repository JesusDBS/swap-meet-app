import pytest
from app.vendor import Vendor
from app.item import Item

def test_swap_first_item_returns_true():
    item_a = Item(category="clothing")
    item_b = Item(category="clothing")
    item_c = Item(category="clothing")
    fatimah = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Item(category="electronics")
    item_e = Item(category="decor")
    jolie = Vendor(
        inventory=[item_d, item_e]
    )

    result = fatimah.swap_first_item(jolie)

    assert len(fatimah.inventory) is 3
    assert item_a not in fatimah.inventory
    assert item_b in fatimah.inventory
    assert item_c in fatimah.inventory
    assert item_d in fatimah.inventory
    assert len(jolie.inventory) is 2
    assert item_d not in jolie.inventory
    assert item_e in jolie.inventory
    assert item_a in jolie.inventory
    assert result is True


def test_swap_first_item_from_my_empty_returns_false():
    fatimah = Vendor(
        inventory=[]
    )

    item_d = Item(category="electronics")
    item_e = Item(category="decor")
    jolie = Vendor(
        inventory=[item_d, item_e]
    )

    result = fatimah.swap_first_item(jolie)

    assert len(fatimah.inventory) is 0
    assert len(jolie.inventory) is 2
    assert result is False


def test_swap_first_item_from_their_empty_returns_false():
    item_a = Item(category="clothing")
    item_b = Item(category="clothing")
    item_c = Item(category="clothing")
    fatimah = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    jolie = Vendor(
        inventory=[]
    )

    result = fatimah.swap_first_item(jolie)

    assert len(fatimah.inventory) is 3
    assert len(jolie.inventory) is 0
    assert result is False
