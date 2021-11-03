import pytest
from app.vendor import Vendor
from app.item import Item
from app.clothing import Clothing
from app.decor import Decor
from app.electronics import Electronics


def test_clothing_has_default_category_and_to_str():
    cloth = Clothing()
    assert cloth.category is "Clothing"
    assert str(cloth) == "The finest clothing you could wear."


def test_decor_has_default_category_and_to_str():
    decor = Decor()
    assert decor.category is "Decor"
    assert str(decor) == "Something to decorate your space."


def test_electronics_has_default_category_and_to_str():
    electronics = Electronics()
    assert electronics.category is "Electronics"
    assert str(electronics) == "A gadget full of buttons and secrets."


def test_items_have_condition_as_float():
    items = [
        Clothing(condition=3.5),
        Decor(condition=3.5),
        Electronics(condition=3.5)
    ]
    for item in items:
        assert item.condition == pytest.approx(3.5)

def test_items_have_condition_descriptions_that_are_the_same_regardless_of_type():
    items = [
        Clothing(condition=5),
        Decor(condition=5),
        Electronics(condition=5)
    ]
    five_condition_description = items[0].condition_description()
    assert type(five_condition_description) == str
    for item in items:
        assert item.condition_description() == five_condition_description

    items[0].condition = 1
    one_condition_description = items[0].condition_description()
    assert type(one_condition_description) == str

    for item in items:
        item.condition = 1
        assert item.condition_description() == one_condition_description

    assert one_condition_description != five_condition_description

