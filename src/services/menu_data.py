import csv
from models.ingredient import Ingredient
from models.dish import Dish


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.load_menu_data(source_path)

    def load_menu_data(self, source_path):
        with open(source_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            self.process_menu_data(reader)

    def process_menu_data(self, reader):
        for row in reader:
            dish_name = row[0]
            dish_price = float(row[1])
            ingredient_name = row[2]
            ingredient_amount = int(row[3])

            dish = self.verify_create_dish(dish_name, dish_price)
            ingredient = Ingredient(ingredient_name)
            dish.add_ingredient_dependency(ingredient, ingredient_amount)

    def verify_create_dish(self, dish_name, dish_price):
        for dish in self.dishes:
            if dish.name == dish_name:
                return dish

        new_dish = Dish(dish_name, dish_price)
        self.dishes.add(new_dish)
        return new_dish
