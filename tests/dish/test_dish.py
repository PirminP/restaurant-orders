import pytest
from src.models.ingredient import (
    Ingredient,
    Restriction
) # noqa: F401, E261, E501
from src.models.dish import Dish  # noqa: F401, E261, E501


# Req 2
def test_dish():
    dish_1 = Dish('Schnitzel de frango', 43.00)
    dish_2 = Dish('Pulled pork', 38.00)
    ingredient_1 = Ingredient('frango')
    ingredient_1_restriction = {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED
    }

    dish_1.add_ingredient_dependency(ingredient_1, 500)

    assert dish_1.name == 'Schnitzel de frango'

    assert hash(dish_1) == hash(Dish('Schnitzel de frango', 43.00))
    assert hash(dish_1) != hash(dish_2)

    assert dish_1 == Dish('Schnitzel de frango', 43.00)
    # assert dish_1 != dish_2

    assert repr(dish_1) == "Dish('Schnitzel de frango', R$43.00)"

    with pytest.raises(
        TypeError, match="Dish price must be float."
    ):
        Dish('Pulled pork', '38.00')

    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish('Chevapchichi', -33)

    assert dish_1.recipe == {ingredient_1: 500}
    assert dish_1.get_ingredients() == {ingredient_1}

    assert dish_1.get_restrictions() == ingredient_1_restriction
