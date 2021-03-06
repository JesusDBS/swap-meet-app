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


def test_get_by_age():
    item_a = Clothing(condition=2.0, age=2)
    item_b = Decor(condition=2.0, age=5)
    item_c = Clothing(condition=4.0, age=2)
    item_d = Decor(condition=5.0, age=2)
    item_e = Clothing(condition=3.0, age=4)
    tai = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )

    result = tai.get_by_age(2)

    assert len(result) is 3
    assert len(tai.get_by_age(4)) is 1


def test_get_by_age_no_match_is_false():
    item_a = Clothing(condition=2.0, age=2)
    item_b = Decor(condition=2.0, age=5)
    item_c = Clothing(condition=4.0, age=2)
    item_d = Decor(condition=5.0, age=2)
    item_e = Clothing(condition=3.0, age=4)
    tai = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )

    result = tai.get_by_age(3)

    assert result is False


def test_newest_swap_by_age_condition():
    item_a = Decor(condition=2.0, age=1)
    item_b = Electronics(condition=4.0)
    item_c = Decor(condition=4.0, age=3)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(condition=2.0, age=2)
    item_e = Decor(condition=4.0)
    item_f = Clothing(condition=4.0, age=1)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    result = tai.swap_by_age_condition(
        other=jesse,
        my_priority="Clothing",
        their_priority="Decor",
        age_condition = 'newest'
    )

    assert result is True
    assert len(tai.inventory) is 3
    assert len(jesse.inventory) is 3
    assert item_a not in tai.inventory
    assert item_f in tai.inventory
    assert item_f not in jesse.inventory
    assert item_a in jesse.inventory


def test_oldest_swap_by_age_condition():
    item_a = Decor(condition=2.0, age=3)
    item_b = Electronics(condition=4.0)
    item_c = Decor(condition=4.0, age=1)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(condition=2.0, age=1)
    item_e = Decor(condition=4.0)
    item_f = Clothing(condition=4.0, age=2)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    result = tai.swap_by_age_condition(
        other=jesse,
        my_priority="Clothing",
        their_priority="Decor",
        age_condition = 'oldest'
    )

    assert result is True
    assert len(tai.inventory) is 3
    assert len(jesse.inventory) is 3
    assert item_a not in tai.inventory
    assert item_f in tai.inventory
    assert item_f not in jesse.inventory
    assert item_a in jesse.inventory


def test_swap_by_old():
    item_a = Decor(condition=2.0, age=1)
    item_b = Electronics(condition=4.0)
    item_c = Decor(condition=4.0, age=3)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(condition=2.0, age=2)
    item_e = Decor(condition=4.0)
    item_f = Clothing(condition=4.0, age=3)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    result = tai.swap_by_old(
        other=jesse,
        my_priority="Clothing",
        their_priority="Decor",
        my_aging_priority =1,
        their_aging_priority=3
    )

    assert result is True
    assert len(tai.inventory) is 3
    assert len(jesse.inventory) is 3
    assert item_a not in tai.inventory
    assert item_f in tai.inventory
    assert item_f not in jesse.inventory
    assert item_a in jesse.inventory


def test_swap_by_old_no_match_is_false():
    item_a = Decor(condition=2.0, age=1)
    item_b = Electronics(condition=4.0)
    item_c = Decor(condition=4.0, age=3)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(condition=2.0, age=2)
    item_e = Decor(condition=4.0)
    item_f = Clothing(condition=4.0, age=3)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    result = tai.swap_by_old(
        other=jesse,
        my_priority="Clothing",
        their_priority="Decor",
        my_aging_priority =1,
        their_aging_priority=4
    )

    assert result is True

  

