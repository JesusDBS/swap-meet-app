import pytest
from app.vendor import Vendor
from app.item import Item

def test_item_overrides_to_string():
    item = Item()

    stringified_item = str(item)

    assert stringified_item == "Hello World!"

def test_swap_items_returns_true():
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

    result = fatimah.swap_items(jolie, item_b, item_d)

    assert len(fatimah.inventory) is 3
    assert item_b not in fatimah.inventory
    assert item_a in fatimah.inventory
    assert item_c in fatimah.inventory
    assert item_d in fatimah.inventory
    assert len(jolie.inventory) is 2
    assert item_d not in jolie.inventory
    assert item_e in jolie.inventory
    assert item_b in jolie.inventory
    assert result is True

def test_swap_items_when_my_item_is_missing_returns_false():
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

    result = fatimah.swap_items(jolie, item_e, item_d)

    assert len(fatimah.inventory) is 3
    assert item_d not in fatimah.inventory
    assert item_a in fatimah.inventory
    assert item_b in fatimah.inventory
    assert item_c in fatimah.inventory
    assert len(jolie.inventory) is 2
    assert item_d in jolie.inventory
    assert item_e in jolie.inventory
    assert result is False

def test_swap_items_when_their_item_is_missing_returns_false():
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

    result = fatimah.swap_items(jolie, item_b, item_c)

    assert len(fatimah.inventory) is 3
    assert item_d not in fatimah.inventory
    assert item_a in fatimah.inventory
    assert item_b in fatimah.inventory
    assert item_c in fatimah.inventory
    assert len(jolie.inventory) is 2
    assert item_d in jolie.inventory
    assert item_e in jolie.inventory
    assert result is False

def test_swap_items_from_my_empty_returns_false():
    fatimah = Vendor(
        inventory=[]
    )

    item_d = Item(category="electronics")
    item_e = Item(category="decor")
    jolie = Vendor(
        inventory=[item_d, item_e]
    )

    nobodys_item = Item(category="clothing")

    result = fatimah.swap_items(jolie, nobodys_item, item_d)

    assert len(fatimah.inventory) is 0
    assert len(jolie.inventory) is 2
    assert result is False

def test_swap_items_from_their_empty_returns_false():
    item_a = Item(category="clothing")
    item_b = Item(category="clothing")
    item_c = Item(category="clothing")
    fatimah = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    jolie = Vendor(
        inventory=[]
    )

    nobodys_item = Item(category="clothing")

    result = fatimah.swap_items(jolie, item_b, nobodys_item)

    assert len(fatimah.inventory) is 3
    assert len(jolie.inventory) is 0
    assert result is False