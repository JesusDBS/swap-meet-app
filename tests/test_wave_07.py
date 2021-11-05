import pytest
from app.vendor import Vendor
from app.item import Item
from app.clothing import Clothing
from app.decor import Decor
from app.electronics import Electronics


def test_get_by_condition():
    item_a = Clothing(condition=2.0)
    item_b = Decor(condition=2.0)
    item_c = Electronics(condition=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    result = tai.get_by_condition(2)

    assert len(result) is 2


def test_get_by_condition_no_match_is_false():
    item_a = Clothing(condition=2.0)
    item_b = Decor(condition=2.0)
    item_c = Electronics(condition=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    result = tai.get_by_condition(3)

    assert result is False


def test_get_by_category_no_match_is_false():
    item_a = Clothing(condition=2.0)
    item_b = Decor(condition=2.0)
    item_c = Electronics(condition=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    result = tai.get_by_category("Candies")

    assert result is False


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


def test_remove_by_category_from_invetory():
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
    assert tai.get_by_category("Electronics") is False


def test_remove_by_category_no_match_is_false():
    item_a = Clothing(condition=2.0)
    item_b = Decor(condition=2.0)
    tai = Vendor(
        inventory=[item_a, item_b]
    )
    result = tai.remove_by_category("Electronics")

    assert result is False
    assert tai.get_by_category("Electronics") is False


def test_remove_by_condition():
    item_a = Clothing(condition=2.0)
    item_b = Decor(condition=2.0)
    item_c = Electronics(condition=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    result = tai.remove_by_condition(2)

    assert result is True
    assert len(tai.inventory) is 1
    assert tai.get_by_condition(2) is False


def test_remove_by_condition_from_category_dictionary():
    item_a = Clothing(condition=2.0)
    item_b = Clothing(condition=1.0)
    item_c = Clothing(condition=5.0)

    item_d = Decor(condition=1.0)
    item_f = Decor(condition=1.0)
    item_g = Decor(condition=2.0)

    item_h = Electronics(condition=1.0)
    item_i = Electronics(condition=1.0)
    item_j = Electronics(condition=4.0)

    tai = Vendor(
        inventory=[
            item_a, item_b, item_c,
            item_d, item_f, item_g,
            item_h, item_i, item_j
        ]
    )

    result = tai.remove_by_condition(1)

    assert result is True
    assert len(tai.inventory) is 4
    assert len(tai._dict_category["Electronics"]) is 1
    assert len(tai._dict_category["Decor"]) is 1
    assert len(tai._dict_category["Clothing"]) is 2
    assert tai.get_by_condition(1) is False


def test_remove_by_condition_no_match_is_false():
    item_a = Clothing(condition=2.0)
    item_b = Decor(condition=2.0)
    item_c = Electronics(condition=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    result = tai.remove_by_condition(3)

    assert result is False
    assert len(tai.inventory) is 3
    assert tai.get_by_condition(3) is False


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
    assert tai.get_by_category("Electronics") is False
    assert "Electronics" not in tai._dict_category.keys()


def test_not_removing_category_with_items_in_inventory():
    item_a = Clothing(condition=2.0)
    item_b = Decor(condition=2.0)
    item_c = Electronics(condition=4.0)
    item_d = Electronics(condition=4.0)

    tai = Vendor(
        inventory=[item_a, item_b, item_c, item_d]
    )
    
    tai.remove(item_c)

    assert len(tai.inventory) is 3
    assert len(tai._dict_category.keys()) is 3
    assert tai.get_by_category("Electronics") is not False
    assert "Electronics" in tai._dict_category.keys()


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






    