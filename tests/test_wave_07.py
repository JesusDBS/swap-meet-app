import pytest
from app.vendor import Vendor
from app.item import Item
from app.clothing import Clothing
from app.decor import Decor
from app.electronics import Electronics

def test_check_length_by_category():
    item_a = Clothing(condition=2.0)
    item_b = Decor(condition=2.0)
    item_c = Clothing(condition=4.0)
    item_d = Decor(condition=5.0)
    item_e = Clothing(condition=3.0)
    item_f = Clothing(condition=3.0)
    item_g = Decor(condition=5.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e, item_f, item_g]
    )

    assert len(tai._dict_category.keys()) is 2
    assert len(tai._dict_category["Clothing"]) is 3
    assert len(tai._dict_category["Decor"]) is 2
    assert "Electronics" not in tai._dict_category.keys()
    assert "Whatever category" not in tai._dict_category.keys()


def test_delete_category_from_invetory():
    item_a = Clothing(condition=2.0)
    item_b = Decor(condition=2.0)
    item_c = Electronics(condition=4.0)
    item_d = Electronics(condition=5.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c, item_d]
    )

    result = tai.remove_by_category("Electronics")

    assert result is True
    assert len(tai.inventory) is 2
    assert len(tai._dict_category.keys()) is 2
    assert "Electronics" not in tai._dict_category.keys()


def test_delete_by_category_no_match_is_false():
    item_a = Clothing(condition=2.0)
    item_b = Decor(condition=2.0)
    tai = Vendor(
        inventory=[item_a, item_b]
    )
    result = tai.remove_by_category("Electronics")

    assert result is False


def test_removing_category_with_no_items_in_inventory():
    item_a = Clothing(condition=2.0)
    item_b = Decor(condition=2.0)
    item_c = Electronics(condition=4.0)

    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )
    
    tai.remove(item_c)

    assert len(tai.inventory) is 2
    assert len(tai._dict_category.keys()) is 2


def test_removing_condition_with_no_items_in_inventory():
    item_a = Clothing(condition=2.0)
    item_b = Decor(condition=2.0)
    item_c = Clothing(condition=4.0)
    item_d = Clothing(condition=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c, item_d]
    )
    tai.remove(item_a)

    assert len(tai.inventory) is 3
    assert len(tai._dict_category.keys()) is 2
    assert len(tai._dict_category["Clothing"]) is 1


def test_when_removing_all_items_from_a_category_delete_category():
    item_a = Clothing(condition=2.0)
    item_b = Decor(condition=2.0)
    item_c = Clothing(condition=4.0)
    item_d = Clothing(condition=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c, item_d]
    )
    tai.remove(item_b)

    assert len(tai.inventory) is 3
    assert "Decor" not in tai._dict_category.keys()
    assert len(tai._dict_category.keys()) is 1






    