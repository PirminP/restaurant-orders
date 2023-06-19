from src.models.ingredient import (
    Ingredient,
    Restriction
) # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient_1 = Ingredient('frango')
    # ingredient_2 = Ingredient('queijo gorgonzola')
    ingredient_1_restriction = {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED
    }

    assert ingredient_1.name == 'frango'
    assert ingredient_1.restrictions == ingredient_1_restriction

    assert ingredient_1 == Ingredient('frango')
    # assert ingredient_1 != ingredient_2

    assert hash(ingredient_1) == hash('frango')
    # assert hash(ingredient_2) != hash('frango')

    assert repr(ingredient_1) == "Ingredient('frango')"
